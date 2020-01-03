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
        pin = settings.NEOPIXEL_PIN
        freq_hz = settings.NEOPIXEL_FREQ_HZ
        dma = settings.NEOPIXEL_DMA
        invert = settings.NEOPIXEL_INVERT
        brightness = settings.NEOPIXEL_BRIGHTNESS
        channel = settings.NEOPIXEL_CHANNEL

        strip = None
        if name.lower() == "neopixel":
            # Create NeoPixel object with appropriate configuration.
            strip = PixelStrip(size, pin, freq_hz, dma, invert, brightness, channel)
            # Intialize the library (must be called once before other functions).
            strip.begin()

        return strip
