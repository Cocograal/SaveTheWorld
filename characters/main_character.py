import characters.player as player


class MainCharacter(player.Player):

    def __init__(self, master, view, name, money, monsters):
        super().__init__(master, view, name, money, monsters)

    def __str__(self):
        return "Player"