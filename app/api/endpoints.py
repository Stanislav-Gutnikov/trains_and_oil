from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.main_sim import main_func
from app.db.db import get_async_session
from app.db.crud import crud
from app.api.validators import (
    is_calc_id_in_db,
    is_same_calc
)


router = APIRouter(
    prefix='/model'
)


@router.get('/', response_class=FileResponse)
async def get_excel(
    calc_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    await is_calc_id_in_db(calc_id, session)
    excel_file_path = await crud.get(calc_id, session)
    headers = {'Content-Disposition': 'attachment; filename="get_db_data.xls"'}
    return FileResponse(
        excel_file_path,
        headers=headers,
        media_type='application/xls'
        )


@router.post('/')
async def create_calc(
    calc_id: int,
    recalc: bool,
    session: AsyncSession = Depends(get_async_session)
):
    if recalc is True:
        await is_calc_id_in_db(calc_id, session)
    else:
        await is_same_calc(calc_id, session)
    await main_func(calc_id, recalc, session)
    return 'Рассчет добавлен'


@router.delete('/all')
async def clear_all(session: AsyncSession = Depends(get_async_session)):
    await crud.delete_all(session)
    return 'Данные очищены'


@router.delete('/')
async def delete_object(
    calc_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    await is_calc_id_in_db(calc_id, session)
    await crud.delete_obj(calc_id, session)
    return 'Данные по заданному id очищены'
