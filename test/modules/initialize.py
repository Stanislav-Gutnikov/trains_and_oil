import yaml
from datetime import datetime
from typing import List

from test.core.route import Route, NewRoute
from test.core.train import Train
from test.core.terminal import Terminal
from test.input.data_from_app import train_list

with open('test/input/input.yaml') as f:
    lst = yaml.safe_load(f)

start_date = datetime(2021, 11, 15, 0, 0, 0)
end_date = datetime(2021, 11, 30, 0, 0, 0)

routes: List[Route] = []
for route in lst['routes']:
    if route.get('dist') is None:
        route = NewRoute(route)
    else:
        route = Route(route)
    routes.append(route)

trains: List[Train] = []
for train in train_list:
    train = Train(train, routes)
    trains.append(train)
for train in trains:
    print(train.name, train.new_route.dist_1, train.new_route.dist_2, train.status)

terminals: List[Terminal] = []
for terminal in lst['terminals']:
    terminal = Terminal(terminal)
    terminals.append(terminal)
