from app.core.terminal import Terminal
from app.core.train import Train
from app.modules.initialize import terminals


polarny = terminals[2]


def simulate_terminal(terminal: Terminal):
    terminal.oil_production()


def simulate_export(train: Train):
    if polarny.oil >= 10000 or train.status == 'loading':
        train.oil_export(polarny)


def simulate_train(train: Train):
    train_terminal_name = train.route.load_point
    terminal = None
    for i in terminals:
        if i.name == train_terminal_name:
            terminal = i
    if train.oil_loading(terminal):
        if train.move():
            if train.oil_unloading(polarny):
                train.move()
