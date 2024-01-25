from typing import Dict, List

from test.core.route import NewRoute
from test.core.route import Route
from test.core.terminal import Terminal


class Train:
    def __init__(
            self,
            train: Dict,
            routes: List[Route]
            ) -> None:
        self.name: str = train.get('name')
        self.oil: int = train.get('oil')
        self.max_oil: int = train.get('max_oil')
        self.dist: int = train.get('dist')
        self.dist_1: int = train.get('dist_1')
        self.dist_2: int = train.get('dist_2')
        self.speed: int = train.get('speed')
        self.route: Route = self.get_route(train.get('route'), routes)
        self.new_route: NewRoute = self.get_route(train.get('new_route'), routes)
        self.status: str = train.get('status')
        self.destination: str = ''
        self.type: str = train.get('type')
        #if self.type != 'export':
            #if self.dist + self.speed < self.route.dist:
                #self.status = 'move'
            

    def get_route(self, train_route, routes):
        for route in routes:
            if route.name == train_route:
                return route

    def move_1(self):
        if self.dist + self.speed <= self.new_route.dist_1 and self.status == 'move_1':
            self.dist += self.speed
        else:
            '''
            if self.oil == self.max_oil:
                self.status = 'unloading'
            if self.oil == 0:
                self.status = 'loading'
                '''
            return self.dist
        
    def move_2(self):
        if self.dist + self.speed <= self.new_route.dist_2 and self.status == 'move_2':
            self.dist += self.speed
        else:
            '''
            if self.oil == self.max_oil:
                self.status = 'unloading'
            if self.oil == 0:
                self.status = 'loading'
                '''
            return self.dist

    def oil_loading_1(
            self,
            terminal: Terminal
            ):
        #if self.name == 'raduzhny_1_light':
            #print(terminal.name)
        if (
            None in terminal.ways.values() and
            self.status != 'unloading' and
            self.status != 'move_1' and
            self.destination != 'zvezda' and
            self.destination != 'polarny'
            #2450 <= self.dist <= 2550
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
                    #if 2450 <= self.dist <= 2550:
                    self.status = 'move_1'
                    self.dist = 0
                    #if 3950 <= self.dist <= 4050:
                        #self.status = 'move_2'
                    self.destination = 'polarny'
                        #self.dist = 0
                    return self
        else:
            return self

    def oil_loading_2(
            self,
            terminal: Terminal
            ):
        #if self.name == 'raduzhny_1_light':
            #print(terminal.name)
        if (
            None in terminal.ways.values() and
            self.status != 'unloading' and
            #self.status != 'move' and
            #self.status != 'move_2' and
            3950 <= self.dist <= 4050
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
                    #if 2450 <= self.dist <= 2550:
                        #self.status = 'move_1'
                        #self.dist = 0
                    #if 3950 <= self.dist <= 4050:
                    self.status = 'move_2'
                    self.dist = 0
                    self.destination = 'polarny'
                    return self
        else:
            return self

    def oil_unloading_1(
            self,
            terminal: Terminal
            ):
        if (
            #self.status != 'move_1' and
            #self.status != 'move_2' and
            self.status == 'move_1' and
            self.destination == 'polarny' and
            2450 <= self.dist <= 2550

        ):
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
                if 2450 <= self.dist <= 2550:
                    self.status = 'move_2'
                    self.dist = 0
                    self.destination = 'zvezda'
                if 3950 <= self.dist <= 4050:
                    self.status = 'move_1'
                    self.dist = 0
                    self.destination = 'raduzhny'
                return self
        else:
            return self
        
    def oil_unloading_2(
            self,
            terminal: Terminal
            ):
        if (
            #self.status != 'move_1' and
            #self.status != 'move_2' and
            self.status != 'loading' and
            self.destination == 'polarny' and 
            3950 <= self.dist <= 4050

        ):
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
                if 2450 <= self.dist <= 2550:
                    self.status = 'move_2'
                    self.dist = 0
                    self.destination = 'zvezda'
                if 3950 <= self.dist <= 4050:
                    self.status = 'move_1'
                    self.dist = 0
                    self.destination = 'raduzhny'
                return self
        else:
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
