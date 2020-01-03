#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glow.effects.bicolor_effect import BicolorEffect


class EffectFactory:
    @staticmethod
    def create(name, **kwargs):

        effect = None

        if name.lower() == "bicolor":
            print(*kwargs["colors"])
            effect = BicolorEffect(name, kwargs["colors"])

        return effect
