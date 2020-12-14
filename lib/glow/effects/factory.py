#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.colors import palette
from glow.effects.breath_dim_effect import BreathDimEffect
from glow.effects.colored_mirror_effect import ColoredMirrorEffect
from glow.effects.colored_wheel_effect import ColoredWheelEffect
from glow.effects.dim_effect import DimEffect
from glow.effects.mirror_effect import MirrorEffect
from glow.effects.ncolor_effect import NColorEffect
from glow.effects.wheel_effect import WheelEffect

logger = logging.getLogger(__name__)


class EffectFactory:
    @staticmethod
    def _get_params(**kwargs):
        """Parse kwargs and return parameters from it"""

        # Color settings
        colors = []
        if "colors" in kwargs:
            colors = [palette[color] for color in kwargs["colors"]]

        ncolors = int(kwargs.get("ncolors", 1))

        # Moves
        offset = int(kwargs.get("offset", 1))
        clockwise = bool(kwargs.get("clockwise", False))
        converge = bool(kwargs.get("converge", True))

        # Dim
        brightness = int(kwargs.get("brightness", 127))
        step = int(kwargs.get("step", 10))

        return dict(
            colors=colors,
            ncolors=ncolors,
            offset=offset,
            clockwise=clockwise,
            converge=converge,
            brightness=brightness,
            step=step,
        )

    @staticmethod
    def create(name, **kwargs):
        effect = None
        logger.debug("Creating effect {}".format(name))

        params = EffectFactory._get_params(**kwargs)

        if name.lower() == "ncolor":
            effect = NColorEffect(
                name, colors=params["colors"], ncolors=params["ncolors"]
            )

        if name.lower() == "wheel":
            effect = WheelEffect(
                name, offset=params["offset"], clockwise=params["clockwise"]
            )

        if name.lower() == "mirror":
            effect = MirrorEffect(
                name, offset=params["offset"], converge=params["converge"]
            )

        if name.lower() == "dim":
            effect = DimEffect(name, brightness=params["brightness"])

        if name.lower() == "breath_dim":
            effect = BreathDimEffect(
                name,
                brightness=params["brightness"],
                step=params["step"],
                clockwise=params["clockwise"],
            )

        if name.lower() == "colored_wheel":
            effect = ColoredWheelEffect(
                name,
                colors=params["colors"],
                ncolors=params["ncolors"],
                offset=params["offset"],
            )

        if name.lower() == "colored_mirror":
            effect = ColoredMirrorEffect(
                name,
                colors=params["colors"],
                ncolors=params["ncolors"],
                offset=params["offset"],
                converge=params["converge"],
            )

        logger.info("Created effect {}".format(effect))
        return effect
