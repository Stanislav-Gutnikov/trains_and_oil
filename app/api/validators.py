from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from http import HTTPStatus

from app.db.models.polarny import Polarny


async def is_calc_id_in_db(
        calc_id: int,
        session: AsyncSession
):
    obj = await session.execute(select(Polarny).where(
                Polarny.calc_id == calc_id
            ))
    obj = obj.scalars().first()
    if obj is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Данные по заданному id не найдены'
        )


async def is_same_calc(
        calc_id: int,
        session: AsyncSession
):
    obj = await session.execute(select(Polarny).where(
                Polarny.calc_id == calc_id
            ))
    obj = obj.scalars().first()
    if obj:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой расчет уже существует'
        )
