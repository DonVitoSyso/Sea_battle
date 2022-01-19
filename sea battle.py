import random

class Dot:
    def __init__(self, x=None, y=None, val='.'):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def get_Dot(self):
        return f'Dot - x:{self.x} y:{self.y}'

class Ship():
    def __init__(self, ship_bow, length=None, orientation=''):
        self.length = length
        # нос коробля калсса Dot(x, y)
        self.ship_bow = ship_bow
        self.orientation = orientation
        self.lives = length

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
    def __init__(self, hid=False, size = 6):
        self.board_ = [["o" for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hid = hid
        self.size = size
        self.count = 0
        # этот тип непонятен
        self.busy = []

    def add_ship(self, length=2):
        i = 30
        ship_tmp = Ship()
        while i:
            # генераторы случайных расположений
            ornt = random.choice("HV")
            x = random.randint(0, 5) if ornt == 'H' else random.randint(0, 5-length)
            y = random.randint(0, 5-length) if ornt == 'H' else random.randint(0, 5)
            # генераторы случайных расположений
            ship = Ship(length, x, y, ornt)
            # сохраняем корабль на доску
            for j in range(len(ship.dots())):
                if self.board_[ship.dots()[j].x][ship.dots()[j].y].val == '.':
                    self.board_[ship.dots()[j].x][ship.dots()[j].y].val = ship.dots()[j].val
                else:
                    i -= 1
                    break
        return i
                # print(ship.dots()[j].val, ship.dots()[j].x, ship.dots()[j].y)

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
        return False if 0 <= dot.x < 6 and 0 <= dot.y < 6 else True

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
ship = Ship(3, 2, 3, "V")

#print(ship.get_Ship(), ship.get_Dot())
#print(*ship.dots())
board = Board(ship, True, 1)
print(board.ships.ship.get_Dot())
# print(board.board_)
# board.show()
board.show()
ship_list = [1, 2, 2, 1, 1, 1, 1]
for s in ship_list:
    print(board.add_ship(s))
board.show()

list_1 = [Dot(y, x) for x, y in zip(range(4), range(4))]
print(list_1)
for i in range(4):
    for j in range(4):
        ...
        # print(list_1[i][j].x, list_1[i][j].y, list_1[i][j].val)
list_2 = [Dot(0,0), Dot(1,1), Dot(1,2)]
# for x in list_2:
#     for y in list_1:
#         for z in y:
#             if x == z:
#                 print("Проверка прошла!", y)

# print(list(filter(lambda i: i in list_2, list_2)))
if all(x in list_1 for x in list_2):
    print("Проверка прошла!")
else:
    print(False)


# сама игра начинатся здесь
game = Game
game.greet()
