#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.wheel_effect import WheelEffect
from glow.effects.bicolor_effect import BicolorEffect

logger = logging.getLogger()


class ColoredWheelEffect(BicolorEffect, WheelEffect):
    """
      TODO: Color -> Mix of both
    """

    def __init__(self, name: str, colors: list, offset=1):
        WheelEffect.__init__(self, name=name, offset=offset)
        BicolorEffect.__init__(self, name=name, colors=colors)
