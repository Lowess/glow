#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

try:
    import RPi.GPIO as GPIO
except ImportError:
    from glow.RPi import GPIO

logger = logging.getLogger(__name__)


class LightManager:
    def __init__(self, lights=None):
        self._lights = []

        if lights is not None:
            for light in lights:
                self.add(light)

        GPIO.setmode(GPIO.BCM)

    def to_json(self):
        lights = []
        for light in self._lights:
            lights.append(light.to_json())

        return lights

    def add(self, light):
        GPIO.setup(light.pin, GPIO.OUT)
        self._lights.append(light)

    def get(self, uid):
        for light in self._lights:
            logger.info(light)
            if str(light.uid) == str(uid):
                return light
        return None

    @property
    def lights(self):
        return self._lights
