import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


load_dotenv()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(os.getenv('TEST_DATABASE_URL'))
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session
