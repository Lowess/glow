#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import math
import atexit
import logging
from logging.config import dictConfig

from flask import Flask, url_for, redirect, render_template, send_from_directory
from dynaconf import LazySettings

from glow.colors import palette
from glow.strips import GlowStrip, StripFactory
from glow.effects import EffectFactory

STRIPS = []


def create_app():

    app = Flask(__name__)

    # Configure Dynaconf
    settings = LazySettings(
        ENVVAR_PREFIX_FOR_DYNACONF="GLOW", ENVVAR_FOR_DYNACONF="GLOW_SETTINGS"
    )

    # Initialize logging
    dictConfig(settings.LOGGING)
    logger = logging.getLogger(__name__)

    logger.info("Glow initialized with: {}".format(settings.to_dict()))

    # Glow setup
    neopixel = StripFactory.create(size=settings.NEOPIXEL_SIZE)

    for strip_settings in settings.GLOW["strips"]:
        logger.debug("Initializig Glow strip with: {}".format(strip_settings))

        # Build the list of effects based on provided settings
        effects = []
        for effect_settings in strip_settings.get("effects", []):
            effect = EffectFactory.create(**effect_settings)
            effects.append(effect)

        gstrip = GlowStrip(
            name=strip_settings.get("name", "unknown"),
            strip=neopixel,
            start=strip_settings["start"],
            stop=strip_settings["stop"],
            effects=effects,
            delay=strip_settings.get("delay", 0),
        )

        colors = []
        logger.info("Fill is {}".format(strip_settings.get("fill", False)))
        if strip_settings.get("fill", False):
            if len(strip_settings["colors"]) > 0:
                fill = math.ceil(len(gstrip) / len(strip_settings["colors"]))
                pattern = [palette[color] for color in strip_settings["colors"] * fill]
                logger.info("Pattern is {0}".format(pattern))
                # fmt:off
                colors = pattern[strip_settings["start"]:strip_settings["stop"]]
                # fmt:on
        else:
            colors = [palette[color] for color in strip_settings["colors"]]

        gstrip.paint(colors)

        STRIPS.append(gstrip)

    # for gstrip in STRIPS:
    #     logger.debug(len(gstrip))

    ################################################################################
    # Blueprints registration
    ################################################################################

    from glow.glow import glow
    from glow.dashboard import dashboard

    app.register_blueprint(glow)
    app.register_blueprint(dashboard)

    @app.template_filter()
    def to_hex(decimal):
        return hex(decimal).split("x")[-1].zfill(6)

    @app.route("/", methods=["GET"])
    def index(error=None):
        return redirect(url_for("glow.show"))

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "img/favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    def cleanup():
        for gstrip in STRIPS:
            gstrip.off()

    atexit.register(cleanup)

    ################################################################################
    # Global errors handling
    ################################################################################

    if not app.config["DEBUG"]:

        @app.errorhandler(500)
        def internal_server_error(error):
            return render_template("error.html", error=str(error), code=500), 500

        @app.errorhandler(404)
        def page_not_found(error):
            return render_template("error.html", error=str(error), code=404), 404

        @app.errorhandler(Exception)
        def exception_handler(error):
            return render_template("error.html", error=error)

    return app
