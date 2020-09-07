#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template

from glow import strip_manager

# Define a blueprint
ui = Blueprint("ui", __name__, url_prefix="/ui")


@ui.route("", methods=["GET"])
def display():
    return render_template("ui/dashboard.html", strips=strip_manager.strips)
