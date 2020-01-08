#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.colors import palette
from glow.effects.dim_effect import DimEffect
from glow.effects.wheel_effect import WheelEffect
from glow.effects.bicolor_effect import BicolorEffect
from glow.effects.breath_dim_effect import BreathDimEffect
from glow.effects.colored_wheel_effect import ColoredWheelEffect

logger = logging.getLogger()


class EffectFactory:
    @staticmethod
    def create(name, **kwargs):

        effect = None
        logger.debug("Creating effect {}".format(name))

        # TODO: Refactor that crap do kwargs at top
        # and agregate color if statement

        if name.lower() == "bicolor":
            colors = []
            if "colors" in kwargs:
                colors = [palette[color] for color in kwargs["colors"]]
            effect = BicolorEffect(name, colors=colors)

        if name.lower() == "wheel":
            effect = WheelEffect(
                name,
                offset=kwargs.get("offset", 1),
                clockwise=kwargs.get("clockwise", False),
            )

        if name.lower() == "dim":
            effect = DimEffect(name, brightness=kwargs.get("brightness", 127))

        if name.lower() == "breath_dim":
            effect = BreathDimEffect(
                name,
                brightness=kwargs.get("brightness", 127),
                step=kwargs.get("step", 10),
                clockwise=kwargs.get("clockwise", True),
            )

        if name.lower() == "colored_wheel":
            colors = []
            if "colors" in kwargs:
                colors = [palette[color] for color in kwargs["colors"]]
            effect = ColoredWheelEffect(
                name, colors=colors, offset=kwargs.get("offset", 1)
            )

        return effect
