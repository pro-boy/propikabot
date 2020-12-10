#  © Pikabot
#
# You may not use this file without proper authorship and consultant from @ItzSjDudeSupport
#
# Made By @ItzSjDude for Pikabot

import threading
from sqlalchemy import func, distinct, Column, String, UnicodeText
from pikabot.sql_helper import SESSION, BASE

class Blfx(BASE):
    __tablename__ = "blacklistx"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, Blfx)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


Blfx.__table__.create(checkfirst=True)


BLACKLIST_FILTER_INSERTION = threading.RLock()

CHAT_BLACKLIST = {}



def a_to_blx(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION:
        blacklist_filt = Blfx(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLIST.setdefault(str(chat_id), set()).add(trigger)


def rf_blx(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION:
        blacklist_filt = SESSION.query(Blfx).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLIST.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLIST.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def gc_blx(chat_id):
    return CHAT_BLACKLIST.get(str(chat_id), set())


def no_blfx():
    try:
        return SESSION.query(Blfx).count()
    finally:
        SESSION.close()


def n_bl_cfx(chat_id):
    try:
        return SESSION.query(Blfx.chat_id).filter(Blfx.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def n_bl_fcx():
    try:
        return SESSION.query(func.count(distinct(Blfx.chat_id))).scalar()
    finally:
        SESSION.close()


def __lc_blx():
    global CHAT_BLACKLIST
    try:
        chats = SESSION.query(Blfx.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLIST[chat_id] = []

        all_filters = SESSION.query(Blfx).all()
        for x in all_filters:
            CHAT_BLACKLIST[x.chat_id] += [x.trigger]

        CHAT_BLACKLIST = {x: set(y) for x, y in CHAT_BLACKLIST.items()}

    finally:
        SESSION.close()


__lc_blx()





