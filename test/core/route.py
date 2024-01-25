from typing import Dict


class Route:
    def __init__(
            self,
            route: Dict
            ) -> None:
        self.name: str = route['name']
        self.dist: int = route.get('dist')
        self.load_point: str = route.get('load_point')
        self.unload_point: str = route.get('unload_point')


class NewRoute:
    def __init__(
            self,
            route: Dict
            ) -> None:
        self.name: str = route['name']
        self.dist_1: int = route['dist_1']
        self.dist_2: int = route['dist_2']
        self.load_point_1: str = route['load_point_1']
        self.load_point_2: str = route['load_point_2']
        self.unload_point: str = route['unload_point']
