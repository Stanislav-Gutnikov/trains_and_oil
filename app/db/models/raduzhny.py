from sqlalchemy import Column, Integer, String, DateTime

from app.db.db import Base


class ProductionPoint(Base):
    __abstract__ = True
    datetime = Column(DateTime)
    oil = Column(Integer)
    train_name = Column(String(100), default='None')
    train_unloading = Column(Integer)
    calc_id = Column(Integer)


class Raduzhny(ProductionPoint):
    pass
