class Vector2f():

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __add__(self, other):
        return Vector2f(self.x1 + other.x1, self.y1 + other.y1,
                        self.x2 + other.x2, self.y2 + other.y2)

    def __str__(self):
        return f"{self.x1}, {self.y1}, {self.x2}, {self.y2}"
