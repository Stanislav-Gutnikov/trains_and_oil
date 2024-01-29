from typing import Dict, List

from app.core.route import Route
from app.core.terminal import Terminal


class Train:
    def __init__(
            self,
            train: Dict,
            route_list: List[Route]
            ) -> None:
        self.name: str = train.get('name')
        self.oil: int = train.get('oil')
        self.max_oil: int = train.get('max_oil')
        self.dist: int = train.get('dist')
        self.speed: int = train.get('speed')
        self.routes: Dict = train.get('routes')
        self.route: Route = self.get_route(train.get('route'), route_list)
        self.status: str = ''
        self.destination: str = ''
        self.type: str = train.get('type')
        self.route_list = route_list
        if self.type != 'export':
            if self.dist + self.speed < self.route.dist:
                self.status = 'move'

    def try_change_route(self, single_date):
        if single_date >= list(self.routes.keys())[1]:
            self_route = list(self.routes.values())[0]
            other_route = list(self.routes.values())[1]
            if self.route != other_route:
                self.route = self.get_route(other_route, self.route_list)         
        return

    def get_route(self, train_route, route_list):
        for route in route_list:
            if route.name == train_route:
                return route

    def move(self):
        if self.dist + self.speed <= self.route.dist and self.status == 'move':
            self.dist += self.speed
        else:
            if self.oil == self.max_oil:
                self.status = 'unloading'
            if self.oil == 0:
                self.status = 'loading'
            return self.dist

    def oil_loading(
            self,
            terminal: Terminal
            ):
        if (
            None in terminal.ways.values() and
            self.status != 'unloading' and
            self.status != 'move'
        ):
            for key, value in terminal.ways.items():
                if value is None:
                    terminal.ways[key] = self
                    break
            self.status = 'loading'

        if self in terminal.ways.values():
            if terminal.oil - terminal.loading < 0 and (
                self.status == 'loading'
            ):
                pass
            if self.oil + terminal.loading <= self.max_oil and (
                terminal.oil - terminal.loading >= 0
            ):
                terminal.oil -= terminal.loading
                self.oil += terminal.loading
            else:
                if self.oil + terminal.loading >= self.max_oil:
                    for key, value in terminal.ways.items():
                        if value == self:
                            terminal.ways[key] = None
                            break
                    self.status = 'move'
                    self.dist = 0
                    return self
        else:
            return self

    def oil_unloading(
            self,
            terminal: Terminal,
            single_date
            ):
        if self.status != 'move' and self.status != 'loading':
            if self not in terminal.ways.values():
                for key, value in terminal.ways.items():
                    if value is None:
                        terminal.ways[key] = self
                        break
                self.status = 'unloading'

        if self in terminal.ways.values():
            if self.oil - terminal.unloading >= 0:
                terminal.oil += terminal.unloading
                self.oil -= terminal.unloading
                return None
            else:
                for key, value in terminal.ways.items():
                    if value == self:
                        terminal.ways[key] = None
                        break
                self.try_change_route(single_date)
                self.status = 'move'
                self.dist = 0
                return self

    def oil_export(
            self,
            terminal: Terminal
            ):
        if (
            None in terminal.ways.values() and
            self not in terminal.ways.values()
        ):
            for key, value in terminal.ways.items():
                if value is None:
                    terminal.ways[key] = self
                    break
            self.status = 'loading'
        if self in terminal.ways.values():
            if terminal.oil - terminal.loading < 0 and (
                self.status == 'loading'
            ):
                pass
            if self.oil + terminal.loading <= self.max_oil and (
                terminal.oil - terminal.loading >= 0
            ):
                terminal.oil -= terminal.loading
                self.oil += terminal.loading
            else:
                if self.oil + terminal.loading >= self.max_oil:
                    for key, value in terminal.ways.items():
                        if value == self:
                            terminal.ways[key] = None
                            break
                    self.status = None
                    self.oil = 0
                    return self
        else:
            return self
