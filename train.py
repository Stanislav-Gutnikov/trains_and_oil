from typing import Dict, List

from route import Route
from terminal import Terminal


class Train:
    def __init__(
            self,
            train: Dict,
            routes: List[Route]
            ) -> None:
        self.name: str = train['name']
        self.oil: int = train['oil']
        self.max_oil: int = train['max_oil']
        self.dist: int = train['dist']
        self.speed: int = train['speed']
        self.route: Route = self.get_route(train['route'], routes)
        self.status: str = ''
        self.destination: str = ''

    def get_route(self, train_route, routes):
        for route in routes:
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
        if len(terminal.ways) < terminal.max_ways and (
            self not in terminal.ways and
            self.status != 'unloading' and
            self.status != 'move'
        ):
            terminal.ways.append(self)
            self.status = 'loading'
            self.dist = 0
        if self in terminal.ways:
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
                    terminal.ways.remove(self)
                    self.status = 'move'
                    return self
        else:
            return self

    def oil_unloading(
            self,
            terminal: Terminal
            ):
        if self.status != 'move' and self.status != 'loading':
            if len(terminal.ways) < terminal.max_ways and (
                self not in terminal.ways
            ):
                terminal.ways.append(self)
                self.status = 'unloading'

        if self in terminal.ways:
            if self.oil - terminal.unloading >= 0:
                terminal.oil += terminal.unloading
                self.oil -= terminal.unloading
                return None
            else:
                terminal.ways.remove(self)
                self.status = 'move'
                self.dist = 0
                return self
