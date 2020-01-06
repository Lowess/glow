#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from abc import ABCMeta
from typing import List

from glow.typing import PixelListType

logger = logging.getLogger()


class Effect(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self._name = name
        self._pixels = None
        self._offsets = None

    def _initialize(self, pixels: PixelListType) -> None:
        self._pixels = list(pixels)
        self._offsets = list()
        for i, _ in enumerate(self._pixels):
            self._offsets.append(i)

    @property
    def pixels(self):
        return self._pixels

    @property
    def offsets(self) -> List[int]:
        return self._offsets

    def colorize(self) -> None:
        pass

    def dim(self) -> None:
        pass

    def offset(self) -> None:
        pass

    def apply(self, pixels: PixelListType) -> PixelListType:
        if self._pixels is None:
            self._initialize(pixels)

        self.colorize()
        self.dim()
        self.offset()

        logger.info("pixels={}".format(self._pixels))

        # Return the new pixels shape
        new_pixels = []

        for offset in self._offsets:
            new_pixels.append(self._pixels[offset])

        logger.info("New pixels after effect apply: {}".format(new_pixels))
        return new_pixels
