#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.wheel_effect import WheelEffect
from glow.effects.ncolor_effect import NColorEffect

logger = logging.getLogger(__name__)


class ColoredWheelEffect(NColorEffect, WheelEffect):
    """
      TODO: Color -> Mix of both
    """

    def __init__(self, name: str, colors: list, ncolors: int = 2, offset=1):
        WheelEffect.__init__(self, name=name, offset=offset)
        NColorEffect.__init__(self, name=name, colors=colors, ncolors=ncolors)
