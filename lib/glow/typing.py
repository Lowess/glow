#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, NewType, TypeVar

from glow.colors import Color
from glow.strips import GlowStrip

PixelType = TypeVar("PixelType", bound=Color)
PixelListType = NewType("PixelListType", List[PixelType])
GlowStripType = TypeVar("GlowStripType", bound=GlowStrip)

__all__ = ["GlowStripType", "PixelType", "PixelListType"]
