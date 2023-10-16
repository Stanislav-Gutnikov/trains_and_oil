import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import Session, sessionmaker, declarative_base, declared_attr


load_dotenv()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(engine, class_=Session)


def get_session():
    with SessionLocal() as session:
        yield session

