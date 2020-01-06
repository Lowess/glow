#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.colors import palette
from glow.effects.wheel_effect import WheelEffect
from glow.effects.bicolor_effect import BicolorEffect

logger = logging.getLogger()


class EffectFactory:
    @staticmethod
    def create(name, **kwargs):

        effect = None
        logger.debug("Creating effect {}".format(name))

        if name.lower() == "bicolor":
            colors = []
            if "colors" in kwargs:
                colors = [palette[color] for color in kwargs["colors"]]
            effect = BicolorEffect(name, colors=colors)
        if name.lower() == "wheel":
            effect = WheelEffect(name, offset=kwargs.get("offset", 1))

        return effect
