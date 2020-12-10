#!/bin/bash
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 
#
# © @ItzSjdude, Made for Pikabot

_logo() {
    echo '
    ╔═╦╦╗───╔╗──╔╗
    ║╬╠╣╠╦═╗║╚╦═╣╚╗
    ║╔╣║═╣╬╚╣╬║╬║╔╣
    ╚╝╚╩╩╩══╩═╩═╩═╝
    '
}

_CleanUp() {
    echo 'Cleaning up Pikabot'
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_UpSource() {
    echo 'Updating PikaBot With ItzSjDude/PikachuUserbot' 
    git clone -b Beta https://github.com/ItzSjDude/PikachuUserbot ./ &> /dev/null
    mkdir ./plugins
    git clone https://github.com/ItzSjDude/PikaBotPlugins ./Temp &> /dev/null
    cp ./Temp/plugins/*.py ./plugins && cp ./Temp/plugins/resources/*.py ./pikabot
    rm -rf ./Temp
}

_UpPip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo '••• Updated Pip •••'
}

StartUp() {
    _logo
    _CleanUp
    _UpSource
    _UpPip
    mkdir ./pikabot/main_plugs
    python3 -m pikabot
}
