from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from http import HTTPStatus

from app.db.models.polarny import Polarny


def is_calc_id_in_db(
        calc_id: int,
        session: Session
):
    obj = session.execute(select(Polarny).where(
                Polarny.calc_id == calc_id
            ))
    obj = obj.scalars().first()
    if obj is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Данные по заданному id не найдены'
        )


def is_same_calc(
        calc_id: int,
        session: Session
):
    obj = session.execute(select(Polarny).where(
                Polarny.calc_id == calc_id
            ))
    obj = obj.scalars().first()
    if obj:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой расчет уже существует'
        )
