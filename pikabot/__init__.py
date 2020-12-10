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

import os; import sys; from telethon.sessions import StringSession; from telethon import TelegramClient; from telethon.tl.types import PeerChannel; from var import Var; from Event_Handlers.logit import *; import time; UpTime = time.time(); from .sql_helper.global_variables import *; from distutils.util import strtobool as sb; import asyncio; import pylast;pk='@'; from pySmartDL import SmartDL;from base64 import b64decode as Pk;from requests import get;import shutil;pid = pika_id+"==" 
print('Optimized Plugins')

#Global Variables
CMD_LIST = {};CMD_HELP = {};Pika_Cmd = {};INT_PLUG = "";LOAD_PLUG = {};COUNT_MSG = 0;USERS = {};COUNT_PM = {};LASTMSG = {};ISAFK = False;AFKREASON = None

ENV = os.environ.get("ENV", False)
if bool(ENV):
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except ValueError:
        pikalog.error("INVALID ID DETECED: Make sure Your I'd starts with -100")
    BOTLOG = sb(os.environ.get("BOTLOG", "False"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    AUTOPIC_COMMENT = os.environ.get("AUTOPIC_COMMENT", "")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", "")
    AUTOPIC_FONT = os.environ.get("AUTOPIC_FONT", "") 
    AUTO_BIO = os.environ.get("AUTO_BIO", "")
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
    DB_URI = os.environ.get("DATABASE_URL", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    MONGO_URI = os.environ.get("MONGO_URI", "")
    CHROME_DRIVER = "/usr/bin/chromedriver"
    GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    COUNTRY = str(os.environ.get("COUNTRY", "India"))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    FBAN_REASON = os.environ.get("FBAN_REASON", None)
    FBAN_USER = os.environ.get("FBAN_USER", None)
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY","./downloads")
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
else:    
    pass

bot= bot2 = bot3 = bot4 = None
BF_BOT=Var.TG_BOT_TOKEN_BF_HER
BF_BOTNAME=Var.TG_BOT_USER_NAME_BF_HER
try:
   if Var.STR1:    
       bot = TelegramClient(StringSession(Var.STR1),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
   if Var.STR2:
       bot2 = TelegramClient(StringSession(Var.STR2),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
   if Var.STR3:
       bot3 = TelegramClient(StringSession(Var.STR3),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
   if Var.STR4:
       bot4 = TelegramClient(StringSession(Var.STR4),Var.APP_ID,Var.API_HASH,auto_reconnect=True)
   if BF_BOT:    
       tgbot = TelegramClient("Tgbot", Var.APP_ID, Var.API_HASH).start(bot_token=BF_BOT)
except:
    pass
