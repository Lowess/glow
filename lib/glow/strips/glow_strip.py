#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from time import sleep

from glow.colors import palette

logger = logging.getLogger(__name__)


class GlowStrip:
    def __init__(
        self, name, strip, start, stop, effects: list = None, delay: float = 0.0
    ):
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._name = name
        self._strip = strip
        self._slice = slice(start, stop)
        self._effects = effects
        self._delay = delay

    def __repr__(self):
        return "<{}>(slice=[{}:{}], effect={})".format(
            self._strip, self._slice.start, self._slice.stop, self._effect
        )

    def __str__(self):
        return "%s" % self._strip

    def __len__(self):
        return self._slice.stop - self._slice.start

    @property
    def name(self):
        return self._name

    @property
    def strip(self):
        return self._strip

    @property
    def start(self):
        return self._slice.start

    @property
    def stop(self):
        return self._slice.stop

    def off(self):
        for i in range(int(self.start), int(self.stop)):
            self._strip.setPixelColor(i, palette["none"])
        self._strip.show()

    def colorize(self, color, start=None, stop=None):
        if start is None:
            start = self.start
        if stop is None:
            stop = self.stop

        logger.info("Colorize from {} -> {}".format(start, stop))
        for i in range(int(start), int(stop)):
            self.strip.setPixelColor(i, color)

    def paint(self, pixels):
        for i, pixel in enumerate(pixels):
            # logger.info("Painting [{}] in {}".format(self.start + i, pixel))
            self._strip.setPixelColor(self.start + i, pixel)

    def dim(self, brightness: int) -> None:
        self._strip.setBrightness(brightness)

    def render(self):
        new_pixels = []
        new_brightness = None

        for effect in self._effects:
            pixels = self._strip.getPixels()
            sub_pixels = list(pixels[self._slice])

            logger.debug(
                "Pixels before {} effect (on {}:{}) -> {}".format(
                    effect, self._slice.start, self._slice.stop, sub_pixels
                )
            )

            new_sub_pixels, new_brightness = effect.apply(sub_pixels)

            logger.debug(
                "Pixels after {} effect (on {}:{}) -> {}".format(
                    effect, self._slice.start, self._slice.stop, new_pixels
                )
            )

            new_pixels += new_sub_pixels

            self.paint(new_sub_pixels)
            self._strip.show()

            logger.info(self)

            if new_brightness is not None:
                logger.debug(
                    "Brightness was changed to {} by {} effect".format(
                        new_brightness, effect
                    )
                )
                self.dim(brightness=new_brightness)

            sleep(self._delay)
        # TODO: If two effects run on the full glow strip
        # new_pixels end up being twice the size. Need to come up
        # with a merge strategy or handle that gracefully

        # logger.info("New pixels len {}".format(len(new_pixels) - len(self)))
        # self.paint(new_pixels[(len(new_pixels) - len(self)) : len(new_pixels)])
        # self._strip.show()
