#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dynaconf import settings

try:
    from rpi_ws281x import PixelStrip
except ImportError:
    from glow.strips.stdout_strip import StdoutPixelStrip as PixelStrip


class StripFactory:
    @staticmethod
    def create(size, name="neopixel"):
        pin = settings.GLOW_PIN
        freq_hz = settings.GLOW_FREQ_HZ
        dma = settings.GLOW_DMA
        invert = settings.GLOW_INVERT
        brightness = settings.GLOW_BRIGHTNESS
        channel = settings.GLOW_CHANNEL

        strip = None
        if name.lower() == "neopixel":
            # Create NeoPixel object with appropriate configuration.
            strip = PixelStrip(size, pin, freq_hz, dma, invert, brightness, channel)
            # Intialize the library (must be called once before other functions).
            strip.begin()

        return strip
