#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from logging.config import dictConfig

from flask import Flask, url_for, redirect, render_template, send_from_directory
from dynaconf import settings

from glow.colors import Color
from glow.displays import GlowStrip
from glow.logging_config import DEFAULT_LOGGING_CONFIG

# Initialize logging
dictConfig(DEFAULT_LOGGING_CONFIG)
logger = logging.getLogger()


def create_app():

    app = Flask(__name__)

    # Make context available in blueprints
    app.app_context().push()

    logger.info("Glow initialized with: {}".format(settings.to_dict()))

    # Switch to [glow] namespace to parse config
    settings.setenv("glow")
    STRIPS = []

    for strip in settings.STRIPS:
        gs = GlowStrip(size=strip["size"])
        gs.render()
        STRIPS.append(gs)

    settings.setenv()
    logger.info(STRIPS)

    for strip in STRIPS:
        strip.colorize(Color(255, 0, 0))
        strip.render()
    ################################################################################
    # Blueprints registration
    ################################################################################

    from glow.displays import display

    app.register_blueprint(display)

    @app.route("/", methods=["GET"])
    def index(error=None):
        return redirect(url_for("display.show"))

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
