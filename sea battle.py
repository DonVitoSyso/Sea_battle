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
    


dot = Dot()
dot.set_Dot(1, 2)
print(dot.get_Dot())
ship = Ship(4, 0, 4, "H", 10)
print(ship.get_Ship(), ship.get_Dot())
print(*ship.dots())
