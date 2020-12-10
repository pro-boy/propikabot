# © 2020 PikaBot
#
# You may not use this file without proper authorship and consent from @ItzSjDudeSupport
#
# Made by @ItzSjDude for Pikabot


from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric
from pikabot.sql_helper import SESSION, BASE


class Snips(BASE):
    __tablename__ = "snips"
    snip = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        snip, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.snip = snip
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference


Snips.__table__.create(checkfirst=True)


def get_snips(keyword):
    try:
        return SESSION.query(Snips).get(keyword)
    except:
        return None
    finally:
        SESSION.close()


def get_all_snips():
    try:
        return SESSION.query(Snips).all()
    except:
        return None
    finally:
        SESSION.close()


def add_snip(keyword, reply, snip_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(Snips).get(keyword)
    if adder:
        adder.reply = reply
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Snips(keyword, reply, snip_type, media_id,
                      media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_snip(keyword):
    note = SESSION.query(Snips).filter(Snips.snip == keyword)
    if note:
        note.delete()
        SESSION.commit()

class Snips2(BASE):
    __tablename__ = "snips2"
    snip = Column(UnicodeText, primary_key=True)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        snip, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None
    ):
        self.snip = snip
        self.reply = reply
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference


Snips2.__table__.create(checkfirst=True)


def get_snips2(keyword):
    try:
        return SESSION.query(Snips2).get(keyword)
    except:
        return None
    finally:
        SESSION.close()


def get_all_snips2():
    try:
        return SESSION.query(Snips2).all()
    except:
        return None
    finally:
        SESSION.close()


def add_snip2(keyword, reply, snip_type, media_id, media_access_hash, media_file_reference):
    adder = SESSION.query(Snips2).get(keyword)
    if adder:
        adder.reply = reply
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Snips2(keyword, reply, snip_type, media_id,
                      media_access_hash, media_file_reference)
    SESSION.add(adder)
    SESSION.commit()


def remove_snip2(keyword):
    note = SESSION.query(Snips2).filter(Snips2.snip == keyword)
    if note:
        note.delete()
        SESSION.commit()
