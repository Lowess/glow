#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template

from glow import STRIPS

# Define a blueprint
dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard.route("", methods=["GET"])
def display():
    return render_template("dashboard.html", strips=STRIPS)
