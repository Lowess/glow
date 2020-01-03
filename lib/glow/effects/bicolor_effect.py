#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from itertools import cycle

from glow.effects.effect import Effect

logger = logging.getLogger()


class BicolorEffect(Effect):
    def __init__(self, name: str, colors: list):
        super().__init__(name)
        self._colors = colors
        self._generator = self._get_color()

    def _get_color(self):
        for color in cycle(self._colors):
            yield color

    def _get_pivot(self, length, depth=1):
        return length / 2

    def apply(self, gstrip):
        pivot = self._get_pivot(len(gstrip))
        logger.info("Pivot is set to {}".format(pivot))
        gen = self._generator
        for i in range(2):
            color = next(gen)
            color_start = (i * pivot) + gstrip.start
            color_stop = ((i + 1) * pivot) + gstrip.start
            logger.info(
                "start={} - stop={} color={}".format(color_start, color_stop, color)
            )
            gstrip.colorize(color=color, start=color_start, stop=color_stop)
