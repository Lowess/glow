#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from itertools import cycle

from glow.effects.effect import Effect

logger = logging.getLogger()


class BicolorEffect(Effect):
    def __init__(self, name: str, colors: list):
        super()
        self._colors = colors
        self._generator = self._get_color()

    def _get_color(self):
        for color in cycle(self._colors):
            yield color

    def _get_pivot(self, length, depth=1):
        return length / 2

    def apply(self, gstrip):
        pivot = self._get_pivot(gstrip.strip.numPixels())
        gen = self._generator
        for i in range(2):
            color = next(gen)
            logger.info(f"{i * pivot} - {i+1 *pivot} {color}")
            gstrip.colorize(color=color, start=(i * pivot), stop=(i + 1) * pivot)
