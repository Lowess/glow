#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.colors import palette

logger = logging.getLogger()


class GlowStrip:
    def __init__(self, strip, start, stop, effects: list = None):
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._strip = strip
        self._slice = slice(start, stop)
        self._effects = effects

    def __repr__(self):
        return "<{}>(slice=[{}:{}], effect={})".format(
            self._strip, self._slice.start, self._slice.stop, self._effect
        )

    def __str__(self):
        return "%s" % self._strip

    def __len__(self):
        return self._slice.stop - self._slice.start

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
            self._strip.setPixelColor(i, color)

    def paint(self, pixels):
        for i, pixel in enumerate(pixels):
            # logger.info("Painting [{}] in {}".format(i, pixel))
            self._strip.setPixelColor(self.start + i, pixel)

    def render(self):
        new_pixels = []
        for effect in self._effects:

            pixels = self._strip.getPixels()
            sub_pixels = list(pixels[self._slice])
            logger.info("Subpixels {}".format(sub_pixels))

            new_sub_pixels = effect.apply(sub_pixels)

            logger.info(
                "Applied {} effect (on {}) -> {}".format(
                    effect._name, self._slice, new_sub_pixels
                )
            )
            new_pixels += new_sub_pixels

        logger.info("New Pixels ({}) ->> {}".format(len(new_pixels), new_pixels))
        self.paint(new_pixels)
        self._strip.show()
