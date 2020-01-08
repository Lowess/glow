#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.dim_effect import DimEffect

logger = logging.getLogger()


class BreathDimEffect(DimEffect):
    def __init__(
        self,
        name: str,
        brightness: int = 127,
        step: int = 10,
        clockwise: bool = True,
        smooth: bool = True,
    ):
        super().__init__(name, brightness=brightness)
        self._step = step
        self._clockwise = -1 if clockwise else +1
        self._smooth = smooth

    def _breath(self):
        new_brightness = self._brightness + (self._step * self._clockwise)
        # If smooth play tick tock effect with clockwise
        if self._smooth:
            if new_brightness < 0 or new_brightness > 255:
                self._clockwise = not self._clockwise

            new_brightness = self._brightness + ((2 * self._step) * self._clockwise)
        else:
            self._brightness = new_brightness % 255

    def dim(self) -> int:
        self._breath()
        return self._brightness
