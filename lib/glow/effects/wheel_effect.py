#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.effect import Effect

logger = logging.getLogger(__name__)


class WheelEffect(Effect):
    def __init__(self, name: str, offset=1, clockwise=True):
        super().__init__(name)
        self._offset = offset
        self._clockwise = clockwise

    def offset(self) -> None:
        for _ in range(self._offset):
            if self._clockwise:
                self._offsets.insert(0, self._offsets.pop(len(self._offsets) - 1))
            else:
                self._offsets.insert(len(self._offsets) - 1, self._offsets.pop(0))

        logger.debug("New offsets {}".format(self._offsets))
