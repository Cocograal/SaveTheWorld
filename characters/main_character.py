import characters.player as player


class MainCharacter(player.Player):

    def __init__(self, master, view, informations):
        super().__init__(master, view, informations)
        self.current_missions = []
        self.finished_missions = []

    def __str__(self):
        return self.name