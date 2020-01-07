#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.effect import Effect

logger = logging.getLogger()


class DimEffect(Effect):
    def __init__(self, name: str, brightness=127):
        super().__init__(name)
        self._brightness = brightness

    def dim(self) -> None:
        return self._brightness
