import util.vector as vector


class Player():

    def __init__(self, master, name, money, monsters):
        self.master = master
        self.name = name
        self.money = money
        self.monsters = monsters

        self.position = vector.Vector2f(240, 240, 260, 260)
        print("PLAYER INITIALISED SUCCESSFULLY")
