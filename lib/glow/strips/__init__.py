#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.strips.glow_strip import GlowStrip

logger = logging.getLogger()
try:
    from rpi_ws281x import PixelStrip
except ImportError:
    logger.warning(
        "rpi_ws281x library is not installed, using StdoutPixelStrip as PixelStrip"
    )
    from glow.strips.stdout_strip import StdoutPixelStrip as PixelStrip


__all__ = ["GlowStrip", "PixelStrip"]
