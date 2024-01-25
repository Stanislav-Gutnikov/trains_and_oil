from test.core.terminal import Terminal
from test.core.train import Train
from test.modules.initialize import terminals


polarny = terminals[2]
zvezda = terminals[1]


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


def new_simulate_train(train: Train):
    train_terminal_name_1 = train.new_route.load_point_1
    train_terminal_name_2 = train.new_route.load_point_2
    terminal_1 = None
    terminal_2 = None
    for i in terminals:
        if i.name == train_terminal_name_1:
            terminal_1 = i
        elif i.name == train_terminal_name_2:
            terminal_2 = i
    if train.name == 'raduzhny_1_light':
        print(train.name, train.dist, train.oil, train.status, terminal_1.name, terminal_1.ways, terminal_2.name, terminal_2.ways)
    if train.oil_loading_1(terminal_1):
        if train.move_1():
            if train.oil_unloading_1(polarny):
                if train.move_2():
                    if train.oil_loading_2(terminal_2):
                        if train.move_2():
                            if train.oil_unloading_2(polarny):
                                train.move_1()

