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
    def __init__(self, length=None, x=None, y=None, orientation="", life=None):
        self.length = length
        super().__init__(x, y)
        self.orientation = orientation
        self.life = life

    def get_Ship(self):
        return f'Ship have length: {self.length} and his position ({self.x}, {self.y})'


dot = Dot()
dot.set_Dot(1, 2)
print(dot.get_Dot())
ship = Ship(10, 0, 10, "h", 10)
print(ship.get_Ship(), ship.get_Dot())
