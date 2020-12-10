# Pikachu Userbot 

<p align="center">
<img src="https://telegra.ph/file/9987086d1312275151b24.png" alt="PIKACHU USERBOT">

ᴀ ᴜꜱᴇʀʙᴏᴛ ᴡɪᴛʜ ʙᴇꜱᴛ ꜰᴇᴀᴛᴜʀᴇꜱ ,ꜱᴇᴄᴜʀɪᴛʏ ᴀɴᴅ ꜱᴏᴍᴇ ꜰᴜɴɴʏ ᴍᴏᴅꜱ ᴛᴏ ʙᴏᴏꜱᴛ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴇxᴘᴇʀɪᴇɴᴄᴇ

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/ItzSjDude/PikachuUserbot)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## **By ItSjDude**
## HOW TO DEPLOY 

## Installing Heroku 

### The Easy Way

**1.Generate String session from** [![Repl.it](https://img.shields.io/badge/REPL%20RUN-Run%20Online-blue.svg)](http://userbot.itzsjdude.repl.run/)

**2.Click on** [![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ItzSjDude/PikachuUserbot)
 
**3.Fill up required fields like Appid,Api hash, String Sesson , Bot token nd Bot username**

**4.Hola! Click on deploy now nd wait for 20-30mins**

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/ItzSjDude/PikachuUserbot
cd PikachuUserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = "Your App Id"
  API_HASH = "Your Api Hash"
```


### Borg Configuration


The Borg Config is situated in `userbot/borgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the Borg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

