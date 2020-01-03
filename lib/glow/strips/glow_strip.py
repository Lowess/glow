#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GlowStrip:
    def __init__(self, strip, effect=None):
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._strip = strip
        self._strip.begin()
        self._effect = effect

    def __repr__(self):
        return "%r" % self._strip

    def __str__(self):
        return "%s" % self._strip.show()

    def __len__(self):
        return self._strip.numPixels()

    @property
    def strip(self):
        return self._strip

    def colorize(self, color, start=0, stop=None):
        if stop is None:
            stop = len(self)
        for i in range(int(start), int(stop)):
            self._strip.setPixelColor(i, color)

    def render(self):
        self._effect.apply(self)
        print(self._strip.show())
