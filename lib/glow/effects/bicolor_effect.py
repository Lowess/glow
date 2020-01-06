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
        self._picker = self._pick()

    def _pick(self):
        for color in cycle(self._colors):
            yield color

    def _get_pivot(self, length, depth=1):
        return length / 2

    def colorize(self) -> None:
        pivot = self._get_pivot(len(self._pixels))
        logger.debug("Pivot is set to {}".format(pivot))

        for i in range(2):
            color = next(self._picker)
            color_start = int(i * pivot)
            color_stop = int((i + 1) * pivot)
            for j in range(color_start, color_stop):
                self._pixels[j] = color
