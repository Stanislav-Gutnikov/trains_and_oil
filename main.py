from dateutil import rrule

from crud import post_to_db
from initialize import (
    start_date,
    end_date,
    trains,
    terminals
)
from simulation import (
    simulate_terminal,
    simulate_export,
    simulate_train
)


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
            post_to_db(terminal, single_date)
        print(single_date)


if __name__ == '__main__':
    main_func()
