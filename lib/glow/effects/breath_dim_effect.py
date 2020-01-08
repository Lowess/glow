#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.dim_effect import DimEffect

logger = logging.getLogger()


class BreathDimEffect(DimEffect):
    def __init__(
        self, name: str, brightness: int = 127, step: int = 10, clockwise: bool = True
    ):
        super().__init__(name, brightness=brightness)
        self._step = step
        self._clockwise = -1 if clockwise else +1

    def _breath(self):
        self._brightness = (self._brightness + (self._step * self._clockwise)) % 255

    def dim(self) -> int:
        self._breath()
        return self._brightness
