#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, jsonify, request
from flask import current_app as app

from glow import light_manager

# Define a blueprint
light = Blueprint("light", __name__, url_prefix="/light")

################################################################################
# main blueprint functions
################################################################################


@light.route("/", methods=["GET"])
def display():
    app.logger.info('[blueprint:main] Hit on "/light" endpoint')
    return jsonify(status="success", lights=light_manager.to_json())


@light.route("/<pin>", methods=["GET", "POST"])
def switch(pin):
    app.logger.info('[blueprint:light] Hit on "/light/{}" endpoint'.format(pin))

    light = light_manager.get(pin)

    if request.method == "POST":
        state = "off"

        data = request.json.get("data", {})
        app.logger.debug("Raw JSON data: {}".format(data))

        if "state" in data:
            state = data["state"]

        app.logger.info(
            "[blueprint:light] Switching {} to state {}".format(light, state)
        )

        if state == "on":
            light.on()
        else:
            light.off()

    if light is None:
        return jsonify(status="error", lights=[])
    else:
        return jsonify(status="success", lights=[light.to_json()])
