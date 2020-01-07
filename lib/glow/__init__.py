#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import atexit
import logging
from logging.config import dictConfig

from flask import Flask, url_for, redirect, render_template, send_from_directory
from dynaconf import LazySettings

from glow.colors import palette
from glow.strips import GlowStrip, StripFactory
from glow.effects import EffectFactory
from glow.logging_config import DEFAULT_LOGGING_CONFIG

# Initialize logging
dictConfig(DEFAULT_LOGGING_CONFIG)
logger = logging.getLogger()

STRIPS = []


def create_app():

    app = Flask(__name__)

    # Configure Dynaconf
    settings = LazySettings(
        ENVVAR_PREFIX_FOR_DYNACONF="GLOW", ENVVAR_FOR_DYNACONF="GLOW_SETTINGS"
    )

    logger.info("Glow initialized with: {}".format(settings.to_dict()))

    # Create the led strip
    neopixel = StripFactory.create(size=settings.NEOPIXEL_SIZE)

    for strip_setting in settings.GLOW["strips"]:
        logger.debug("Initializig Glow strip with: {}".format(strip_setting))

        # Build the list of effects based on provided settings
        effects = []
        for effect in strip_setting["effects"]:
            effect = EffectFactory.create(**effect)
            effects.append(effect)

        gstrip = GlowStrip(
            strip=neopixel,
            start=strip_setting["start"],
            stop=strip_setting["stop"],
            effects=effects,
        )

        colors = [palette[color] for color in strip_setting["colors"]]
        gstrip.paint(colors)

        STRIPS.append(gstrip)

    for gstrip in STRIPS:
        logger.debug(len(gstrip))

    ################################################################################
    # Blueprints registration
    ################################################################################

    from glow.glow import glow

    app.register_blueprint(glow)

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
