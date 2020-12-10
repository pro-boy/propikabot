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

from Event_Handlers import * 

async def pika_login(_PiKa_):
    _PikaBot_ = await TelegramClient(
        "PikaBot",
        Var.APP_ID,
        Var.API_HASH
    ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
    _cn_=get_client(_PiKa_)
    async with _PikaBot_:
        me = await _PikaBot_.get_me()
        pikalog.info(me.first_name)
        @_PikaBot_.on(events.NewMessage())
        async def handler(event):
            APP_ID = Var.APP_ID;API_HASH = Var.API_HASH
            Config=app.config()  
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message(_phone_.format(_cn_))
                pikalog.info("{}:Enter Your Phone No.".format(_cn_))
                pikaget = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                pikares = await pikaget
                phone = pikares.message.message.strip()
                pika_client = TelegramClient(
                    StringSession(),
                    api_id=APP_ID,
                    api_hash=API_HASH
                )
                await pika_client.connect()
                sent = await pika_client.send_code_request(phone)
                await conv.send_message(_verif_.format(_cn_))
                pikalog.info("{}: Please enter the verification code, by giving space. If your code is 6969 then Enter 6 9 6 9".format(_cn_))
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                r_code = response.message.message.strip()
                _2vfa_code_ = None
                r_code = "".join(r_code.split(" "))
                try:
                    await pika_client.sign_in(phone, code=r_code, password=_2vfa_code_)
                    s_string = pika_client.session.save()
                    pika_me = await pika_client.get_me()
                    await conv.send_message(_logged_.format(_cn_,pika_me.first_name))
                    pikalog.info(f"Successfully Logged in as {pika_me.first_name}")
                    Config[_PiKa_] = s_string
                except PhoneCodeInvalidError:
                    pikalog.info(_code_.format(_cn_))
                    await conv.send_message(_code_.format(_cn_,))
                    return
                except SessionPasswordNeededError:
                    pikalog.info("{}: 2-Step verification Protected Account, Enter Your Password".format(_cn_))
                    await conv.send_message(_2vfa_.format(_cn_))
                    response = conv.wait_event(events.NewMessage(
                        chats=event.chat_id
                    ))
                    response = await response
                    _2vfa_code_ = response.message.message.strip()
                    await pika_client.sign_in(password=_2vfa_code_)
                    pika_me = await pika_client.get_me()
                    pikalog.info(f"Successfully Logged in as {pika_me.first_name}")
                    s_string = pika_client.session.save()
                    await conv.send_message(_logged_.format(_cn_,pika_me.first_name))
                    Config[_PiKa_] = s_string
              
        await _PikaBot_.run_until_disconnected()
