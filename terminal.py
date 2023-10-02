from typing import Dict


class Terminal:
    def __init__(
            self,
            terminal: Dict
            ) -> None:
        self.name: str = terminal.get('name')
        self.oil: int = terminal.get('oil')
        self.max_oil: int = terminal.get('max_oil')
        self.production: int = terminal.get('production')
        self.unloading: int = terminal.get('unloading')
        self.loading: int = terminal.get('loading')
        self.ways: Dict = {}
        self.max_ways: int = terminal.get('max_ways')
        self.type: str = terminal.get('type')
        if len(self.ways) == 0:
            for i in range(1, self.max_ways+1):
                self.ways[i] = None

    def oil_production(self):
        self.oil += self.production
        return self.oil

