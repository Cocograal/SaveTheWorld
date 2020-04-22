import util.vector as vector


class Player():

    def __init__(self, master, view, name, money, monsters):
        self.msater = master
        self.view = view
        self.name = name
        self.money = money
        self.monsters = monsters

        self.position = vector.Vector2f(530, 305, 570, 345)
        print(f"{self} INITIALISED SUCCESSFULLY")
