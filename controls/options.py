class Option():
    def __init__(self, master, controler_board, view):
        self.master = master
        self.controler_board = controler_board
        self.view = view

    def change_movement_speed(self, time):
        try:
            time = int(time)
        except ValueError:
            pass
        else:
            self.controler_board.movement_time = time
            self.master.label["text"] = time
