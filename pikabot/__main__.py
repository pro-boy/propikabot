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

import os, telethon, telethon.utils, asyncio, traceback ; from sys import * ;from pikabot import * ;from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import *;a = Pk(pid).decode('utf-8');Client = pk+a

if bot is None: 
    from pikabot.login import *
    _Pika_Loop_ = asyncio.get_event_loop()
    _Pika_Loop_.run_until_complete(pika_login("STRING_SESSION"))
else:
    l= Var.CUSTOM_CMD
    from pikabot import LOGS as pikalog
    from pikabot.login import pika_login
    async def connecting_clients():
        import glob;path = './plugins/*.py';files = glob.glob(path)
        if bot: 
            try: 
                 await bot.start()
                 pikalog.info("_MAINCLIENT_: Connected 🔥")
                 bot.me = await bot.get_me() 
                 bot.uid = telethon.utils.get_peer_id(bot.me)
            except:
                 pikalog.info("**MAINCLIENT**: Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                 await pika_login("STRING_SESSION")
        if bot2:
            try:
                await bot2.start()
                pikalog.info("_MULTICLIENT1_: Connected 🔥")
                bot2.me = await bot2.get_me() 
                bot2.uid = telethon.utils.get_peer_id(bot2.me)
            except:
                pikalog.info("_MULTICLIENT1_: Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR2")
        if bot3:
            try:
                await bot3.start()
                pikalog.info("_MULTICLIENT2_: Connected 🔥")
                bot3.me = await bot.get_me() 
                bot3.uid = telethon.utils.get_peer_id(bot3.me)
            except:
                pikalog.info("_MULTICLIENT2_: Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR3")
        if bot4:
            try:
                await bot4.start()
                pikalog.info("_MULTICLIENT3_: Connected 🔥")
                bot4.me = await bot4.get_me() 
                bot4.uid = telethon.utils.get_peer_id(bot4.me)
            except:
                pikalog.info("_MULTICLIENT3_: Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
                await pika_login("STR4")

        if Var.STR1 and bot is None:
           try:
              await bot.start()
           except:
              pikalog.info("**MAINCLIENT**: Session Expired, Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
              await pika_login("STRING_SESSION")

        if Var.STR2 and bot2 is None:
           try:
              await bot2.start()
           except:
              pikalog.info("**MULTICLIENT1**: Session Expired, Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
              await pika_login("STR2")

        if Var.STR3 and bot3 is None:
           try:
              await bot3.start()
           except:
              pikalog.info("**MULTICLIENT2**: Session Expired, Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
              await pika_login("STR3")

        if Var.STR4 and bot4 is None:
           try:
              await bot4.start()
           except:
              pikalog.info("**MULTICLIENT3**: Session Expired, Started Login Assistent, Do /start at {}'s PM".format(BF_BOTNAME))
              await pika_login("STR4")

        cli1 = await client.get_messages(Client, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
        for ixo in total_doxx:
           mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(Client, ids=mxo), "pikabot/main_plugs")
  
        from pikabot.utils import load_module
        for name in files:
            with open(name) as f:
                path1 = Path(f.name);shortname = path1.stem
                load_module(shortname.replace(".py", ""))

        import pikabot._core

    client.loop.run_until_complete(connecting_clients())

    if len(argv) not in (1, 3, 4):
        ItzSjdude.disconnect()
    else:
        ItzSjDude.run_until_disconnected()

    

