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
        pin = settings["glow"]["neopixel"]["pin"]
        freq_hz = settings["glow"]["neopixel"]["freq_hz"]
        dma = settings["glow"]["neopixel"]["dma"]
        invert = settings["glow"]["neopixel"]["invert"]
        brightness = settings["glow"]["neopixel"]["brightness"]
        channel = settings["glow"]["neopixel"]["channel"]

        strip = None
        if name.lower() == "neopixel":
            # Create NeoPixel object with appropriate configuration.
            strip = PixelStrip(size, pin, freq_hz, dma, invert, brightness, channel)
            # Intialize the library (must be called once before other functions).
            strip.begin()

        return strip
