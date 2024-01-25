from sqlalchemy import Column, Integer, String, DateTime

from test.db.db import Base


class Polarny(Base):
    datetime = Column(DateTime)
    oil = Column(Integer)
    train_name_1 = Column(String(100), default='None')
    train_1_unloading = Column(Integer)
    train_name_2 = Column(String(100), default='None')
    train_2_unloading = Column(Integer)
    train_name_3 = Column(String(100), default='None')
    train_3_unloading = Column(Integer)
    calc_id = Column(Integer)
