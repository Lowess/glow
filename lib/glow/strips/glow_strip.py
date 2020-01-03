#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger()


class GlowStrip:
    def __init__(self, strip, start, stop, effect=None):
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._strip = strip
        self._strip.begin()
        self._start = start
        self._stop = stop
        self._effect = effect

    def __repr__(self):
        return "<{}>(start={}, stop={}, effect={})".format(
            self._strip, self._start, self._stop, self._effect
        )

    def __str__(self):
        return "%s" % self._strip.show()

    def __len__(self):
        return self._stop - self._start

    @property
    def strip(self):
        return self._strip

    @property
    def start(self):
        return self._start

    @property
    def stop(self):
        return self._stop

    def colorize(self, color, start=None, stop=None):
        if start is None:
            start = self._start
        if stop is None:
            stop = self._stop

        logger.info("Colorize from {} -> {}".format(start, stop))
        for i in range(int(start), int(stop)):
            self._strip.setPixelColor(i, color)

    def render(self):
        logger.debug("Applying effect {}".format(self._effect._name))
        self._effect.apply(self)
        print(self._strip.show())
