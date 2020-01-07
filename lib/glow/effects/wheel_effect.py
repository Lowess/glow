#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.effect import Effect

logger = logging.getLogger()


class WheelEffect(Effect):
    def __init__(self, name: str, offset=1, clockwise=True):
        super().__init__(name)
        self._offset = offset
        self._position = 0
        self._clockwise = -1 if clockwise else +1

    def offset(self) -> None:
        for i in range(len(self._offsets)):
            self._offsets[i] = (
                self._offsets[i] + (self._clockwise * self._offset)
            ) % len(self._offsets)
        logger.info("New offsets {}".format(self._offsets))
