#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colors import color

from glow.colors import Color


class StdoutPixelStrip(object):
    def __init__(
        self,
        num,
        pin,
        freq_hz=800000,
        dma=10,
        invert=False,
        brightness=255,
        channel=0,
        strip_type=None,
        gamma=None,
    ):
        """Class to represent a SK6812/WS281x LED display.  Num should be the
        number of pixels in the display, and pin should be the GPIO pin connected
        to the display signal line (must be a PWM pin like 18!).  Optional
        parameters are freq, the frequency of the display signal in hertz (default
        800khz), dma, the DMA channel to use (default 10), invert, a boolean
        specifying if the signal line should be inverted (default False), and
        channel, the PWM channel to use (defaults to 0).
        """

        if gamma is None:
            # Support gamma in place of strip_type for back-compat with
            # previous version of forked library
            if type(strip_type) is list and len(strip_type) == 256:
                gamma = strip_type
                strip_type = None
            else:
                gamma = list(range(256))

        # Create ws2811_t structure and fill in parameters.
        self._leds = [Color(0, 0, 0)] * num

        # Initialize the channel in use
        self._channel = channel

    def __repr__(self):
        return "<%r>" % self

    def __str__(self):
        return self.show()

    def _cleanup(self):
        pass

    def setGamma(self, gamma):
        pass

    def begin(self):
        """Initialize library, must be called once before other functions are
        called.
        """
        pass

    def show(self):
        """Update the display with the data from the LED buffer."""
        display = []

        for i, _ in enumerate(self._leds):
            c = self.getPixelColorRGB(i)
            display.append(color("▢".format(idx=i), bg=(c.r, c.g, c.b)))

        return "|" + "|".join(display) + "|"

    def setPixelColor(self, n, color):
        """Set LED at position n to the provided 24-bit color value (in RGB order).
        """
        self._leds[n] = color

    def setPixelColorRGB(self, n, red, green, blue):
        """Set LED at position n to the provided red, green, and blue color.
        Each color component should be a value from 0 to 255 (where 0 is the
        lowest intensity and 255 is the highest intensity).
        """
        self._leds[n] = Color(red, green, blue)

    def getBrightness(self):
        pass

    def setBrightness(self, brightness):
        """Scale each LED in the buffer by the provided brightness.  A brightness
        of 0 is the darkest and 255 is the brightest.
        """
        pass

    def getPixels(self):
        """Return an object which allows access to the LED display data as if
        it were a sequence of 24-bit RGB values.
        """
        return self._leds

    def numPixels(self):
        """Return the number of pixels in the display."""
        return len(self._leds)

    def getPixelColor(self, n):
        """Get the 24-bit RGB color value for the LED at position n."""
        return self._leds[n]

    def getPixelColorRGB(self, n):
        c = lambda: None  # noqa:E731
        setattr(c, "r", self._leds[n] >> 16 & 0xFF)
        setattr(c, "g", self._leds[n] >> 8 & 0xFF)
        setattr(c, "b", self._leds[n] & 0xFF)
        return c
