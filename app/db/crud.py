from datetime import datetime
from sqlalchemy import select
from fastapi import HTTPException
from http import HTTPStatus

from app.core.terminal import Terminal
from app.core.train import Train
from app.db.db import SessionLocal
from app.db.models.polarny import Polarny
from app.db.models.raduzhny import Raduzhny
from app.db.models.zvezda import Zvezda


def get_train_name(train: Train):
    train_name = None
    if train is not None:
        train_name = train.name
    return train_name


def crud_transshipment_point(
    terminal: Terminal,
    start_date: datetime,
    calc_id: int
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
        calc_id=calc_id
    )
    with SessionLocal() as session:
        calculation = session.execute(
            select(Polarny).where(
                Polarny.calc_id == calc_id,
                Polarny.datetime == start_date
            )
        )
        if calculation is None:
            session.add(new_obj)
        else:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Рассчет с таким id уже есть'
            )
        session.commit()
    return


def crud_production_point(
    terminal: Terminal,
    start_date: datetime,
    calc_id: int
):
    if terminal.name == 'raduzhny':
        new_obj = Raduzhny(
            datetime=start_date,
            oil=terminal.oil,
            train_name=get_train_name(terminal.ways.get(1)),
            train_unloading=terminal.unloading,
            calc_id=calc_id
        )
    else:
        new_obj = Zvezda(
            datetime=start_date,
            oil=terminal.oil,
            train_name=get_train_name(terminal.ways.get(1)),
            train_unloading=terminal.unloading,
            calc_id=calc_id
        )
    with SessionLocal() as session:
        session.add(new_obj)
        session.commit()
    return


def post_to_db(
    terminal: Terminal,
    start_date: datetime,
    calc_id: int
):
    if terminal.type != 'transshipment_point':
        crud_production_point(terminal, start_date, calc_id)
    else:
        crud_transshipment_point(terminal, start_date, calc_id)
    return
