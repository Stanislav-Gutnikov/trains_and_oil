from sqlalchemy import Column, Integer, String, DateTime

from test.db.db import Base


class Train(Base):
    datetime = Column(DateTime)
    name = Column(String(100))
    oil = Column(Integer)
    max_oil = Column(Integer)
    dist = Column(Integer)
    speed = Column(Integer)
    route = Column(String(100))
    new_route = Column(String(100))
    status = Column(String(100))
    destination = Column(String(100))
    type = Column(String(100))
    calc_id = Column(Integer)
