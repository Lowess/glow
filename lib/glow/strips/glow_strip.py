#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dynaconf import settings

from glow.strips import PixelStrip


class GlowStrip:
    def __init__(self, size, effect=None):
        pin = settings.GLOW_PIN
        freq_hz = settings.GLOW_FREQ_HZ
        dma = settings.GLOW_DMA
        invert = settings.GLOW_INVERT
        brightness = settings.GLOW_BRIGHTNESS
        channel = settings.GLOW_CHANNEL

        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._strip = PixelStrip(size, pin, freq_hz, dma, invert, brightness, channel)
        self._strip.begin()
        self._effect = effect

    def __repr__(self):
        return "%r" % self._strip

    def __str__(self):
        return "%s" % self._strip.show()

    def colorize(self, color):
        for i in range(self._strip.numPixels()):
            self._strip.setPixelColor(i, color)

    def render(self):
        print(self._strip.show())
