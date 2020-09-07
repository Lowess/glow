#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 :synopsis: Display Blueprint

 Display endpoint of the application
"""

import logging

# Import flask dependencies
from flask import Blueprint, jsonify, request

from glow import scheduler, strip_manager

# Define a blueprint
glow = Blueprint("glow", __name__, url_prefix="/glow")

logger = logging.getLogger(__name__)


@glow.route("/", methods=["GET"])
def json():
    return jsonify(strips=strip_manager.to_json())


@glow.route("", methods=["POST"])
def schedule():
    """
        Schedule a glow strip to periodically run rendering steps.
    """
    if request.method == "POST":
        payload = request.get_json(force=True)
        logger.debug(payload)
        state = payload["state"]
        strip = payload["strip"]

        for gstrip in strip_manager.strips:
            logger.info(f"{gstrip.name} - {strip}")
            if gstrip.name == strip:
                if state == "on":
                    scheduler.add_job(
                        id=gstrip.name,
                        func=gstrip.render,
                        trigger="interval",
                        seconds=1,
                    )
                elif state == "on":
                    scheduler.remove_job(id=gstrip.name)

        return jsonify(status="success", msg="{} is {}".format(strip, state))
