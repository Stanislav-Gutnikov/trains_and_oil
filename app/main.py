from dateutil import rrule
from fastapi import FastAPI, APIRouter

from app.db.crud import post_to_db
from app.modules.initialize import (
    start_date,
    end_date,
    trains,
    terminals
)
from app.modules.simulation import (
    simulate_terminal,
    simulate_export,
    simulate_train
)

'''Если роутер кладу в api/endpoints то оттуда мне нужно вызвать main_func -> Ошибка импорта Error loading ASGI app. Could not import module "app.main".
   Можно main_func переложить в modules?'''
router = APIRouter(
    prefix='/model'
)


@router.post('/')
def create_calc(
    calc_id: int
):
    main_func(calc_id)
    return 'Рассчет добавлен'


app = FastAPI(title='Симуляция логистической системы')
app.include_router(router)


def main_func(calc_id: int):
    for single_date in rrule.rrule(
        rrule.HOURLY,
        dtstart=start_date,
        until=end_date
    ):
        for terminal in terminals:
            simulate_terminal(terminal)
        for train in trains:
            if train.type == 'transport':
                simulate_train(train)
            else:
                simulate_export(train)
        for terminal in terminals:
            post_to_db(terminal, single_date, calc_id)
        print(single_date)


# if __name__ == '__main__':
    # main_func()
