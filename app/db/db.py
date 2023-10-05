import os
import psycopg2
from psycopg2.errors import Error
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

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres') # в .env
SessionLocal = sessionmaker(engine, class_=Session)



'''Ниже не нужно'''


def db(sql: str):
    try:
        connect = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
            )
        cursor = connect.cursor()
        # connect.autocommit = True
        cursor.execute(sql)
        connect.commit()
        connect.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


    
sql_1 = '''CREATE TABLE zvezda
(date timestamp,
oil int,
production int,
way_1_train varchar,
way_1_unloading int)'''


#db(sql_1)
