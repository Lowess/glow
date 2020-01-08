#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.effect import Effect

logger = logging.getLogger(__name__)


class MirrorEffect(Effect):
    def __init__(self, name: str, offset=1, converge=True):
        super().__init__(name)
        self._offset = offset
        self._converge = converge

    def __str__(self):
        return "{} (offset={}, converge={})".format(
            super().__str__(), self._offset, self._converge
        )

    def _mirror_center(self, size):
        if size % 2 == 1:
            return round(size / 2) + 1
        else:
            return round(size / 2)

    def offset(self) -> None:
        midpoint = self._mirror_center(len(self._offsets))
        logger.info("Midpoint {}".format(midpoint))

        # Split
        l_offsets = self._offsets[0:midpoint]
        # fmt:off
        r_offsets = self._offsets[midpoint:len(self._offsets)]
        # fmt:on
        for _ in range(self._offset):
            if self._converge:
                l_offsets.insert(0, l_offsets.pop())
                r_offsets.insert(len(r_offsets), r_offsets.pop(0))
            else:
                l_offsets.insert(len(l_offsets), l_offsets.pop(0))
                r_offsets.insert(0, r_offsets.pop())

        self._offsets = l_offsets + r_offsets

        logger.info("New offsets {}".format(self._offsets))
