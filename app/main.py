from dateutil import rrule
from fastapi import FastAPI

from app.db.crud import post
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


app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'}


def main_func():
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
            post(terminal, single_date) # ф-ция db каждый раз открывает и закрывает курсор?, медленно. с сессией то же самое, но через сессию намного быстрее
        
        print(single_date)


if __name__ == '__main__':
    main_func()
