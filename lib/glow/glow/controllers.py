#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 :synopsis: Display Blueprint

 Display endpoint of the application
"""

from datetime import datetime

# Import flask dependencies
from flask import Blueprint, jsonify

from glow import STRIPS

# Define a blueprint
glow = Blueprint("glow", __name__, url_prefix="/glow")


@glow.route("", methods=["GET"])
def show():
    """
        Returns a simple JSON string when the application is healthy.

        :returns: json -- A JSON with the following format:
        ``{"status": "success",
           "msg": "Glow is glowing",
           "time": "<datetime.now()>"}``
    """
    # app.logger.debug(STRIPS)

    strips = []

    for gstrip in STRIPS:
        gstrip.render()
        if len(strips) == 0:
            strips.append(gstrip.strip.getPixels())

    return jsonify(
        status="success", msg="Glow is glowing", time=str(datetime.now()), strips=strips
    )
