import yaml
from datetime import datetime
from typing import List

from route import Route
from train import Train
from terminal import Terminal

with open('trains_and_oil/input.yaml') as f: # убрать trains_and_oil/
    lst = yaml.safe_load(f)

start_date = datetime(2021, 11, 1, 0, 0, 0)
end_date = datetime(2021, 11, 15, 0, 0, 0)

routes: List[Route] = []
for route in lst['routes']:
    route = Route(route)
    routes.append(route)

trains: List[Train] = []
for train in lst['trains']:
    train = Train(train, routes)
    trains.append(train)

terminals: List[Terminal] = []
for terminal in lst['terminals']:
    terminal = Terminal(terminal)
    terminals.append(terminal)
