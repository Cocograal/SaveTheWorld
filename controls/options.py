import tkinter as tk


class MenuOptions(tk.Menu):
    def __init__(self, master, controler_board, view):
        super().__init__(master=master)
        self.controler_board = controler_board
        self.view = view

        self.add_command(label="Options", command=self.open_menu)

    def open_menu(self):
        self.view.open_menu(self)

    def change_movement_speed(self, time):
        try:
            time = int(time)
        except ValueError:
            pass
        else:
            self.controler_board.movement_time = time
