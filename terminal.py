from typing import Dict, List


class Terminal:
    def __init__(
            self,
            terminal: Dict
            ) -> None:
        self.name: str = terminal['name']
        self.oil: int = terminal['oil']
        self.max_oil: int = terminal['max_oil']
        self.production: int = terminal['production']
        self.unloading: int = terminal['unloading']
        self.loading: int = terminal['loading']
        self.ways: List = []
        self.max_ways: int = terminal['max_ways']

    def oil_production(self):
        self.oil += self.production
        return self.oil
