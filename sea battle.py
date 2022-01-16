import random

class Dot:
    def __init__(self, x=None, y=None, val='.'):
        self.x = y
        self.y = x
        self.val = val

    def __eq__(self, other):
        return True if self.dot == other.dot else False

    def set_Dot(self, x, y):
        self.dot = [x, y]

    def get_Dot(self):
        return f'x:{self.x} y:{self.y} - val:{self.val}'

class Ship():
    def __init__(self, length=None, x=None, y=None, orientation='', life=None):
        self.length = length
        self.ship = Dot(x, y)
        self.orientation = orientation
        self.life = life

    def get_Ship(self):
        return f'Ship have length: {self.length} and his position ({self.ship.dot[0]}, {self.ship.dot[1]})'

    def dots(self):
        dots_ = []
        if self.orientation == "H":
            for h in range(self.length):
                dots_.append(Dot(self.ship.x + h, self.ship.y, '+'))
            # dots_.append(list(Dot(self.ship.x + h, self.ship.y, '+')) for h in range(0, self.length))
        elif self.orientation == "V":
            for v in range(0, self.length):
                dots_.append(Dot(self.ship.x, self.ship.y + v, '+'))
            # dots_ = Dot((self.ship.dot[0], self.ship.dot[1] + v, '+') for v in range(0, self.length))
        return dots_

class Board():
    def __init__(self, ships=Ship(), hid=False, ships_life=0):
        self.board_ = [[Dot() for _ in range(6)] for _ in range(6)]
        # self.board_ = [Dot() for _ in range(6)]
        # for j in range(6):
        #     self.board_[j] = [Dot() for _ in range(6)]
        # self.board_ = [[Dot(0, 0)]*6 for _ in range(36)]
        self.ships = ships
        self.hid = hid
        self.ships_life = ships_life

    def add_ship(self):
        i = 6
        while i > 0:
            i -= 1
            # генераторы случайных расположений
            ornt = random.choice("HV")
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            # генераторы случайных расположений
            length = self.ships.length
            ship = Ship(length, x, y, ornt, length)
            # сохраняем корабль на доску
            for j in range(len(ship.dots())):
                self.board_[ship.dots()[j].x - 1][ship.dots()[j].y - 1].val = ship.dots()[j].val
                # print(ship.dots()[j].val, ship.dots()[j].x, ship.dots()[j].y)
            # for i in range(0, length):
            #     self.board_ = [Dot(x, y, '+')]


    def contour(self):
        ...

    def show(self):
        # print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
        # print("---+---+---+---+---+---+---+")
        # for i in range(0, 6):
        #     print(f' {i+1} ', end='|')
        #     for j in range(0, 6):
        #         print(f' {self.board_[j].dot[0]} ', end='|')
        #     print('\n---+---+---+---+---+---+---+')
        print("    1  2  3  4  5  6 ")
        for i in range(0, 6):
            print(f' {i + 1} ', end='')
            for j in range(0, 6):
                print(f' {self.board_[i][j].val} ', end='')
            print()

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

    def greet():
        ...

    def loop(self):
        ...

    def start(self):
        ...


board_test = [[] for _ in range(0, 6)]
print(board_test)
ship = Ship(3, 2, 3, "V", 3)

#print(ship.get_Ship(), ship.get_Dot())
#print(*ship.dots())
board = Board(ship, True, 1)
print(board.ships.ship.get_Dot())
# print(board.board_)
# board.show()
board.show()
board.add_ship()
board.show()

# сама игра начинатся здесь
game = Game
game.greet()
