import psycopg2
from psycopg2.errors import Error


def db(sql: str):
    try:
        connect = psycopg2.connect(
            database='postgres',
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            port='5432'
            )
        cursor = connect.cursor()
        # connect.autocommit = True
        cursor.execute(sql)
        connect.commit()
        connect.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


sql_1 = '''CREATE TABLE polarny
(date timestamp,
oil int,
production int,
way_1_train varchar,
way_1_unloading int,
way_2_train varchar,
way_2_unloading int,
way_3_train varchar,
way_3_unloading int)'''


# db(sql_1)
