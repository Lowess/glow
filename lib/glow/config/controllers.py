#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, jsonify
from glow.conf import settings

# Define a blueprint
config = Blueprint("config", __name__, url_prefix="/config")


@config.route("", methods=["GET"])
@config.route("/", methods=["GET"])
def display():
    return jsonify(settings.as_dict())
