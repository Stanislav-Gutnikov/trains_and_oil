from dateutil import rrule

from crud import post_to_db
from terminal import Terminal
from train import Train
from initialize import (
    start_date,
    end_date,
    trains,
    terminals
)


polarny = terminals[2]


def simulate_terminal(terminal: Terminal):
    terminal.oil_production()


def simulate_train(train: Train):
    train_terminal_name = train.route.load_point
    terminal = None
    for i in terminals:
        if i.name == train_terminal_name:
            terminal = i
    if train.oil_loading(terminal):
        if train.move():
            if train.oil_unloading(polarny):
                train.move()


def main_func():
    for single_date in rrule.rrule(
        rrule.HOURLY,
        dtstart=start_date,
        until=end_date
        ):
        for terminal in terminals:
            simulate_terminal(terminal)
            post_to_db(terminal, single_date)
        for train in trains:
            if train.type == 'transport':
                simulate_train(train)
            else:
                if polarny.oil >= 10000 or train.status == 'loading':
                    train.oil_export(polarny)
        print(single_date)


if __name__ == '__main__':
    main_func()