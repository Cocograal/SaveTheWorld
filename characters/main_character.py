import characters.player as player


class MainCharacter(player.Player):

    def __init__(self, game_control_board, view, informations):
        super().__init__(game_control_board, view, informations)
        self.current_missions = dict()
        self.finished_missions = []

    def __str__(self):
        return self.name

    def start_mission(self, goal):
        self.current_missions[goal[0]] = goal[-1]

    def update_mission(self, update):
        self.current_missions[update[0]] -= update[-1]
        print(self.current_missions)
