#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from abc import ABCMeta
from typing import List

from glow.typing import PixelListType

logger = logging.getLogger(__name__)


class Effect(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self._name = name
        self._pixels = None
        self._offsets = None
        self._brightness = None

    def __str__(self):
        return "{} (pixels={}, offsets={}, brightness={})".format(
            self._name.capitalize(), self._pixels, self._offsets, self._brightness
        )

    def _initialize(self, pixels: PixelListType) -> None:
        self._pixels = list(pixels)
        if self._offsets is None:
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

    def dim(self) -> int:
        return self._brightness

    def offset(self) -> None:
        pass

    def apply(self, pixels: PixelListType) -> PixelListType:
        # if self._pixels is None:
        self._initialize(pixels)

        self.colorize()
        brightness = self.dim()
        self.offset()

        logger.info("pixels={}".format(self._pixels))

        # Return the new pixels shape
        new_pixels = []

        for offset in self._offsets:
            new_pixels.append(self._pixels[offset])

        return (new_pixels, brightness)
