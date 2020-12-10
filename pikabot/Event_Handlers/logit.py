#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

import os, sys;from logging import basicConfig, getLogger, INFO, DEBUG
_debug = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if _debug:
  _level = DEBUG
else:
  _level = INFO 

basicConfig(format="◆━%(name)s━◆ ◉━%(levelname)s━◉  ⎝✧%(message)s✧⎠",level=_level,)
getLogger("telethon.statecache").setLevel(logging.ERROR)
getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
getLogger("telethon.statecache").setLevel(logging.ERROR)
getLogger("telethon.client.users").setLevel(logging.ERROR)
getLogger("telethon.client.downloads").setLevel(logging.ERROR)
getLogger("telethon.client.telegrambaseclient").setLevel(logging.ERROR)
getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
pikalog = LOGS = getLogger(__name__)
