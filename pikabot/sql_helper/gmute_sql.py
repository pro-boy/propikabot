# © 2020 PikaBot
#
# You may not use this file without proper authorship and consent from @ItzSjDudeSupport
#
# Made by @ItzSjDude for Pikabot

try:
    from pikabot.sql_helper import SESSION, BASE
except ImportError:
    raise Exception("Hello!")

from sqlalchemy import Column, String, UnicodeText


class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GMute.__table__.create(checkfirst=True)


def is_gmuted(sender_id):
    try:
        return SESSION.query(GMute).all()
    except:
        return None
    finally:
        SESSION.close()


def gmute(sender):
    adder = GMute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender):
    rem = SESSION.query(GMute).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

class GMute2(BASE):
    __tablename__ = "gmute2"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GMute2.__table__.create(checkfirst=True)


def is_gmuted2(sender_id):
    try:
        return SESSION.query(GMute2).all()
    except:
        return None
    finally:
        SESSION.close()


def gmute2(sender):
    adder = GMute2(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute2(sender):
    rem = SESSION.query(GMute2).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
