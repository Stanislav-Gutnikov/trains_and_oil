from datetime import datetime

from app.core.terminal import Terminal
from app.core.train import Train
from app.db.db import SessionLocal, db
from app.db.models.polarny import Polarny
from app.db.models.raduzhny import Raduzhny
from app.db.models.zvezda import Zvezda


'''у новых ф-ций непонятные названия.
   Старые ф-ции не нужны
   Исправлю. + по pep8 сделать'''


def get_train_name(train: Train):
    train_name = None
    if train is not None:
        train_name = train.name
    return train_name


def crud_transhhipment_point(
        terminal: Terminal,
        start_date: datetime
        ):
    train_name_1 = get_train_name(terminal.ways.get(1))
    train_name_2 = get_train_name(terminal.ways.get(2))
    train_name_3 = get_train_name(terminal.ways.get(3))
    sql = f'''INSERT INTO {terminal.name} (
        datetime,
        oil,
        train_1_name,
        train_1_unloading,
        train_2_name,
        train_2_unloading,
        train_3_name,
        train_3_unloading)
        VALUES (
            '{start_date}',
            {terminal.oil},
            {terminal.production},
            '{train_name_1}',
            {terminal.unloading},
            '{train_name_2}',
            {terminal.unloading},
            '{train_name_3}',
            {terminal.unloading}
            );'''
    return sql


def crud_production_point(
        terminal: Terminal,
        start_date: datetime
        ):
    if len(terminal.ways) != 0:
        train_name = get_train_name(terminal.ways.get(1))
    sql = f'''INSERT INTO {terminal.name} (
        datetime,
        oil,
        train_name,
        train_unloading)
        VALUES (
            '{start_date}',
            {terminal.oil},
            {terminal.production},
            '{train_name}',
            {terminal.loading}
            );'''
    return sql


def post_to_db(
        terminal: Terminal,
        start_date: datetime
        ):
    if terminal.type != 'transshipment_point':
        sql = crud_production_point(terminal, start_date)
    else:
        sql = crud_transhhipment_point(terminal, start_date)
    db(sql)
    return


def crud_tp(
        terminal: Terminal,
        start_date: datetime  
    ):
    new_obj = Polarny(
        datetime=start_date,
        oil=terminal.oil,
        train_name_1=get_train_name(terminal.ways.get(1)),
        train_1_unloading=terminal.unloading,
        train_name_2=get_train_name(terminal.ways.get(2)),
        train_2_unloading=terminal.unloading,
        train_name_3=get_train_name(terminal.ways.get(3)),
        train_3_unloading=terminal.unloading,
    )
    with SessionLocal() as session:
        session.add(new_obj)
        session.commit()
    return

'''Я тут заношу данные по именам терминалов. Если не понять имя я не смогу понять в какую таблицу занести данные. 
   Как избежать?'''
def crud_p(
        terminal: Terminal,
        start_date: datetime  
    ):
    if terminal.name == 'raduzhny':
        new_obj = Raduzhny(
            datetime=start_date,
            oil=terminal.oil,
            train_name=get_train_name(terminal.ways.get(1)),
            train_unloading=terminal.unloading
        )
    else:
        new_obj = Zvezda(
            datetime=start_date,
            oil=terminal.oil,
            train_name=get_train_name(terminal.ways.get(1)),
            train_unloading=terminal.unloading
        )
    with SessionLocal() as session:
        session.add(new_obj)
        session.commit()
    return



def post(
        terminal: Terminal,
        start_date: datetime  
    ):
    if terminal.type != 'transshipment_point':
        crud_p(terminal, start_date)
    else:
        crud_tp(terminal, start_date)
    return

