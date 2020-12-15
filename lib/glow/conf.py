#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from dynaconf import Dynaconf

BASE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    environments=True, includes=[f"{BASE}/settings.toml", "~/.glow/settings.toml"]
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
