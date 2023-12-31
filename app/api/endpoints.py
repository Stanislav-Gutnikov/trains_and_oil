from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.modules.main_sim import main_func
from app.db.db import get_session
from app.db.crud import crud
from app.api.validators import (
    is_calc_id_in_db,
    is_same_calc
)


router = APIRouter(
    prefix='/model'
)


@router.get('/', response_class=FileResponse)
def get_excel(
    calc_id: int,
    session: Session = Depends(get_session)
):
    is_calc_id_in_db(calc_id, session)
    excel_file_path = crud.get(calc_id, session)
    headers = {'Content-Disposition': 'attachment; filename="get_db_data.xls"'}
    return FileResponse(
        excel_file_path,
        headers=headers,
        media_type='application/xls'
        )


@router.post('/')
def create_calc(
    calc_id: int,
    recalc: bool,
    session: Session = Depends(get_session)
):
    if recalc is True:
        is_calc_id_in_db(calc_id, session)
    else:
        is_same_calc(calc_id, session)
    main_func(calc_id, recalc, session)
    return 'Рассчет добавлен'


@router.delete('/all')
def clear_all(session: Session = Depends(get_session)):
    crud.delete_all(session)
    return 'Данные очищены'


@router.delete('/')
def delete_object(
    calc_id: int,
    session: Session = Depends(get_session)
):
    is_calc_id_in_db(calc_id, session)
    crud.delete_obj(calc_id, session)
    return 'Данные по заданному id очищены'
