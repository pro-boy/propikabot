import os 
from heroku_config import client1 as Client
 
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config

Var = Config
