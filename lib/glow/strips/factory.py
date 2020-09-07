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
        pin = settings.GLOW.NEOPIXEL.PIN
        freq_hz = settings.GLOW.NEOPIXEL.FREQ_HZ
        dma = settings.GLOW.NEOPIXEL.DMA
        invert = settings.GLOW.NEOPIXEL.INVERT
        brightness = settings.GLOW.NEOPIXEL.BRIGHTNESS
        channel = settings.GLOW.NEOPIXEL.CHANNEL

        strip = None
        if name.lower() == "neopixel":
            # Create NeoPixel object with appropriate configuration.
            strip = PixelStrip(size, pin, freq_hz, dma, invert, brightness, channel)
            # Intialize the library (must be called once before other functions).
            strip.begin()

        return strip
