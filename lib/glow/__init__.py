#!/usr/bin/env python
# -*- coding: utf-8 -*-
import atexit
import logging
import math
import os
from logging.config import dictConfig

from apscheduler.schedulers import SchedulerAlreadyRunningError
from flask import Flask, redirect, render_template, send_from_directory, url_for
from flask_apscheduler import APScheduler
from flask_cors import CORS
from glow.colors import palette
from glow.conf import settings
from glow.effects import EffectFactory
from glow.light import Light, LightManager
from glow.strips import GlowStrip, StripFactory, StripManager

# from glow.scheduler import init_scheduler
light_manager = LightManager()
strip_manager = StripManager()
scheduler = APScheduler()
# init_scheduler(scheduler)

# Initialize logging
dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)


def create_app():

    app = Flask(__name__)
    CORS(app)
    logger.info("Glow initialized with: {}".format(settings.to_dict()))

    # ApsScheduler
    try:
        scheduler.init_app(app)
        scheduler.start()
    except SchedulerAlreadyRunningError:
        pass

    # Glow setup
    neopixel = StripFactory.create(size=settings["glow"]["neopixel"]["size"])

    # Strip setup
    for strip_settings in settings["glow"]["strips"]:
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

        strip_manager.add(gstrip)

    # Light setup
    # for light in STRIPS:
    #     logger.debug(len(gstrip))

    for light in settings["glow"]["lights"]:
        light_obj = Light(**light)
        light_manager.add(light_obj)

    ################################################################################
    # Blueprints registration
    ################################################################################

    from glow.config import config
    from glow.glow import glow
    from glow.light.controllers import light
    from glow.ui import ui

    app.register_blueprint(glow)
    app.register_blueprint(light)
    app.register_blueprint(ui)
    app.register_blueprint(config)

    @app.template_filter()
    def to_hex(decimal):
        return hex(decimal).split("x")[-1].zfill(6)

    @app.route("/", methods=["GET"])
    def index(error=None):
        return redirect(url_for("ui.display"))

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "img/favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    def cleanup():
        for gstrip in strip_manager.strips:
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
