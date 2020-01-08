#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from itertools import cycle

from glow.effects.effect import Effect

logger = logging.getLogger(__name__)


class NColorEffect(Effect):
    def __init__(self, name: str, colors: list, ncolors: int = 2):
        super().__init__(name)
        self._ncolors = ncolors
        self._colors = colors
        self._picker = self._pick()

    def __str__(self):
        return "{} (ncolors={}, colors={})".format(
            super().__str__(), self._ncolors, self._colors
        )

    def _pick(self):
        for color in cycle(self._colors):
            yield color

    def colorize(self) -> None:
        color = None

        for i in range(len(self._pixels)):
            if (i % self._ncolors) == 0:
                color = next(self._picker)

            self._pixels[i] = color
