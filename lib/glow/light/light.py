#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

try:
    import RPi.GPIO as GPIO
except ImportError:
    from glow.RPi import GPIO


class LightState(Enum):
    ON = True
    OFF = False


class Light(object):
    def __init__(self, uid, name, pin):
        # Create NeoPixel object with appropriate configuration.
        # Intialize the library (must be called once before other functions).
        self._uid = uid
        self._name = name
        self._pin = pin
        self._state = LightState.OFF

    def __repr__(self):
        return "<{}>(uid={}, name={}, pin={}, state={})".format(
            self._uid, self._name, self._pin, self._state
        )

    def __str__(self):
        return "[id={}] Light {} -> {}".format(self._uid, self._name, self._state)

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @property
    def pin(self):
        return self._pin

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val: LightState):
        self._state = val
        GPIO.output(self._pin, val.value)

    def toggle(self):
        self.state = not self._state

    def on(self):
        self.state = LightState.ON

    def off(self):
        self.state = LightState.OFF

    def to_json(self):
        return {
            "uid": self._uid,
            "name": self._name,
            "pin": self._pin,
            "state": self._state.value,
        }
