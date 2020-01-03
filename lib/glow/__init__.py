#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from logging.config import dictConfig

from flask import Flask, url_for, redirect, render_template, send_from_directory
from dynaconf import settings

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

    # Make context available in blueprints
    app.app_context().push()

    logger.info("Glow initialized with: {}".format(settings.to_dict()))

    # Switch to [glow] namespace to parse config
    settings.setenv("glow")

    for _, strip in settings.STRIPS.items():
        neopixel = StripFactory.create(size=strip["stop"] - strip["start"])

        effect_params = {"colors": [palette[color] for color in strip.effects.colors]}
        effect = EffectFactory.create(name=strip.effects.effect, **effect_params)
        gstrip = GlowStrip(
            strip=neopixel, start=strip["start"], stop=strip["stop"], effect=effect
        )
        STRIPS.append(gstrip)
    settings.setenv()
    logger.info(STRIPS)

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
