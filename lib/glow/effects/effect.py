#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Effect(metaclass=ABCMeta):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def apply(self, strip):
        raise NotImplementedError("You must implement ``apply()``")
