import yaml
from datetime import datetime
from typing import List

from app.core.route import Route
from app.core.train import Train
from app.core.terminal import Terminal

with open('app/input/input.yaml') as f:
    lst = yaml.safe_load(f)

start_date = datetime(2021, 11, 1, 0, 0, 0)
end_date = datetime(2021, 11, 30, 0, 0, 0)

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
