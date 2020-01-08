#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from glow.effects.mirror_effect import MirrorEffect
from glow.effects.ncolor_effect import NColorEffect

logger = logging.getLogger(__name__)


class ColoredMirrorEffect(NColorEffect, MirrorEffect):
    """
      TODO: Color -> Mix of both
    """

    def __init__(
        self, name: str, colors: list, ncolors: int = 2, offset=1, converge=True
    ):
        NColorEffect.__init__(self, name=name, colors=colors, ncolors=ncolors)
        MirrorEffect.__init__(self, name=name, offset=offset, converge=converge)
