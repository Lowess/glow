# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Gunicorn configuration file
  > http://docs.gunicorn.org/en/stable/settings.html#settings.
  Usage: -c 'python:harvest.gunicorn'
"""

from os import environ
from multiprocessing import cpu_count

bind = "0.0.0.0:" + environ.get("HARVEST_PORT", "5000")
preload_app = True
max_requests = 1000
workers = cpu_count()
