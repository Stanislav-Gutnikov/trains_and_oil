from datetime import timedelta
import csv
from db import db

from initialize import (
    start_date,
    end_date,
    trains,
    terminals
)


polarny = terminals[2]


def simulate_terminal(terminal):
    terminal.oil_production()


def simulate_train(train):
    train_terminal_name = train.route.load_point
    terminal = None
    for i in terminals:
        if i.name == train_terminal_name:
            terminal = i
    if train.oil_loading(terminal):
        if train.move():
            if train.oil_unloading(polarny):
                train.move()


with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    while start_date < end_date:
        for terminal in terminals:
            simulate_terminal(terminal)
            if terminal.name != 'polarny':
                train_name = None
                if len(terminal.ways) != 0:
                    train_name = terminal.ways[0].name
                sql = f'''INSERT INTO {terminal.name} (
                    date,
                    oil,
                    production,
                    way_1_train,
                    way_1_unloading)
                    VALUES (
                        '{start_date}',
                        {terminal.oil},
                        {terminal.production},
                        '{train_name}',
                        {terminal.loading}
                        );'''
            else:
                train_name_1 = None
                train_name_2 = None
                train_name_3 = None
                if len(terminal.ways) == 1:
                    train_name_1 = terminal.ways[0].name
                elif len(terminal.ways) == 2:
                    train_name_1 = terminal.ways[0].name
                    train_name_2 = terminal.ways[1].name
                elif len(terminal.ways) == 3:
                    train_name_1 = terminal.ways[0].name
                    train_name_2 = terminal.ways[1].name
                    train_name_3 = terminal.ways[2].name
                sql = f'''INSERT INTO polarny (
                    date,
                    oil,
                    production,
                    way_1_train,
                    way_1_unloading,
                    way_2_train,
                    way_2_unloading,
                    way_3_train,
                    way_3_unloading)
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
            db(sql)
        for train in trains:
            simulate_train(train)
            '''Все что касается вывода в .csv не нужно'''
            writer.writerow([
                start_date,
                train.name,
                train.oil,
                train.dist,
                train.status,
                terminals[0].ways,
                terminals[0].oil
                ])
        print(start_date)
        start_date += timedelta(hours=1)
