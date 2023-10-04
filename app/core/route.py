from typing import Dict


class Route:
    def __init__(
            self,
            route: Dict
            ) -> None:
        self.name: str = route['name']
        self.dist: int = route['dist']
        self.load_point: str = route['load_point']
        self.unload_point: str = route['unload_point']
