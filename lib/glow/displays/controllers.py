#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 :synopsis: Display Blueprint

 Display endpoint of the application
"""

from datetime import datetime

# Import flask dependencies
from flask import Blueprint, jsonify
from flask import current_app as app

# Define a blueprint
display = Blueprint("display", __name__, url_prefix="/display")


@display.route("", methods=["GET"])
def show():
    """
        Returns a simple JSON string when the application is healthy.

        :returns: json -- A JSON with the following format:
        ``{"status": "success",
           "msg": "Glow is healthy",
           "time": "<datetime.now()>"}``
    """
    app.logger.debug("Display")
    return jsonify(status="success", msg="Glow is healthy", time=str(datetime.now()))
