#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class StripManager:
    def __init__(self, strips=None):
        self._strips = [] if strips is None else strips

    def to_json(self):
        strips = []
        for strip in self._strips:
            strips.append(strip.to_json())

        return strips

    def add(self, strip):
        self._strips.append(strip)

    @property
    def strips(self):
        return self._strips
