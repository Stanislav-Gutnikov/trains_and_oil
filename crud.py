from datetime import datetime

from db import db
from terminal import Terminal
from train import Train


def get_train_name(train: Train):
    train_name = None
    if train is not None:
        train_name = train.name
    return train_name


def crud_transhhipment_point(
        terminal: Terminal,
        start_date: datetime
        ):
    train_name_1 = get_train_name(terminal.ways.get(1))
    train_name_2 = get_train_name(terminal.ways.get(2))
    train_name_3 = get_train_name(terminal.ways.get(3))
    sql = f'''INSERT INTO {terminal.name} (
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
    return sql


def crud_production_point(
        terminal: Terminal,
        start_date: datetime
        ):
    if len(terminal.ways) != 0:
        train_name = get_train_name(terminal.ways.get(1))
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
    return sql


def post_to_db(
        terminal: Terminal,
        start_date: datetime
        ):
    if terminal.type != 'transshipment_point':
        sql = crud_production_point(terminal, start_date)
    else:
        sql = crud_transhhipment_point(terminal, start_date)
    db(sql)
