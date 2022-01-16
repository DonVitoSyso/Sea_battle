class Dot:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def set_Dot(self, x, y):
        self.x = x
        self.y = y

    def get_Dot(self):
        return f'x:{self.x} y:{self.y}'

class Ship(Dot):
    dots_ = None
    def __init__(self, length=None, x=None, y=None, orientation="", life=None):
        self.length = length
        super().__init__(x, y)
        self.orientation = orientation
        self.life = life

    def get_Ship(self):
        return f'Ship have length: {self.length} and his position ({self.x}, {self.y})'

    def dots(self):
        if self.orientation == "H":
            dots_ = tuple((self.x + h, self.y) for h in range(0, self.length))
        elif self.orientation == "V":
            dots_ = tuple((self.x, self.y + h) for h in range(0, self.length))
        return dots_

class Board(Ship):
    def __init__(self, ships=[], hid=False, ships_life=0):
        self.board_ = [[]]*36
        self.ships = ships
        self.hid = hid
        self.ships_life = ships_life

    def add_ship(self):
        ...

    def contour(self):
        ...

    def show(self):
        ...

    def out(self, dot):
        return False if 0 < dot.x < 6 and 0 < dot.y < 6 else True

    def shot(self):
        ...

class Player(Board):
    def __init__(self, board_player1, board_player2):
        self.board_player1 = Ship(board_player1)
        self.board_player2 = Ship(board_player2)

    def ask(self):
        ...

    def move(self):
        ...

class user(Player):
    def ask(self):
        ...

class AI(Player):
    def ask(self):
        ...

class Game(Player):
    player1 = user
    board1 = Board()
    player2 = AI
    board2 = Board()

    def random_board(self):
        ...

    def greet(self):
        ...

    def loop(self):
        ...

    def start(self):
        ...


dot = Dot()
dot.set_Dot(1, 2)
print(dot.get_Dot())
ship = Ship(4, 0, 4, "H", 10)
print(ship.get_Ship(), ship.get_Dot())
print(*ship.dots())
board = Board(ship)
print(board.board_)
