#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.strips.factory import StripFactory
from glow.strips.glow_strip import GlowStrip
from glow.strips.manager import StripManager

logger = logging.getLogger()

try:
    from rpi_ws281x import PixelStrip

    HAS_RPI_WS281X = True
except ImportError:
    HAS_RPI_WS281X = False
    logger.warning(
        "rpi_ws281x library is not installed, using StdoutPixelStrip as PixelStrip"
    )
    from glow.strips.stdout_strip import StdoutPixelStrip as PixelStrip

__all__ = ["GlowStrip", "PixelStrip", "StripFactory", "StripManager"]
