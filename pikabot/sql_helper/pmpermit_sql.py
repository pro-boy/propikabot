from sqlalchemy import Column, String
from pikabot.sql_helper import SESSION, BASE

class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason

PMPermit.__table__.create(checkfirst=True)

class PMPermit2(BASE):
    __tablename__ = "pmpermit2"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason

PMPermit2.__table__.create(checkfirst=True)

class PMPermit3(BASE):
    __tablename__ = "pmpermit3"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason

PMPermit3.__table__.create(checkfirst=True)

class PMPermit4(BASE):
    __tablename__ = "pmpermit4"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))

    def __init__(self, chat_id, reason=""):
        self.chat_id = chat_id
        self.reason = reason

PMPermit4.__table__.create(checkfirst=True)

def is_client_approved(chat_id):
    try:
        return SESSION.query(PMPermit2).filter(PMPermit2.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()

def clientapprove(chat_id, reason):
    adder = PMPermit2(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()

def clientdisapprove(chat_id):
    rem = SESSION.query(PMPermit2).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_approved_clients():
    rem = SESSION.query(PMPermit2).all()
    SESSION.close()
    return rem

def is_approved(chat_id):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()

def approve(chat_id, reason):
    adder = PMPermit(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id):
    rem = SESSION.query(PMPermit).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_all_approved():
    rem = SESSION.query(PMPermit).all()
    SESSION.close()
    return rem

def is_approved(chat_id):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()

def is_client3_approved(chat_id):
    try:
        return SESSION.query(PMPermit3).filter(PMPermit3.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()

def client3approve(chat_id, reason):
    adder = PMPermit3(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()

def client3disapprove(chat_id):
    rem = SESSION.query(PMPermit3).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_approved_client3():
    rem = SESSION.query(PMPermit3).all()
    SESSION.close()
    return rem

def is_client4_approved(chat_id):
    try:
        return SESSION.query(PMPermit4).filter(PMPermit4.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()

def client4approve(chat_id, reason):
    adder = PMPermit4(str(chat_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()

def client4disapprove(chat_id):
    rem = SESSION.query(PMPermit4).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_approved_client4():
    rem = SESSION.query(PMPermit4).all()
    SESSION.close()
    return rem
