#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""WSGI callable."""

import gunicorn.app.wsgiapp as wsgi
from glow import create_app  # noqa: F401

wsgi.run()
