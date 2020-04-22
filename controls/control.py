import tkinter as tk
import view.gui as gui
import game



class Control(tk.Tk):

    DIRECTION = {"a": "west",
                 "s": "south",
                 "d": "east",
                 "w": "north"}

    def __init__(self):
        super().__init__()
        self.view = gui.View(self)
        self.game = game.Game(self, self.view)

        self.already_moving = False
        self.key_pressed = None
        self.bind("<KeyPress>", lambda event: self.key_press(event))
        self.bind("<KeyRelease>", lambda event: self.key_release(event))

    def key_press(self, event):
        if event.keysym in self.DIRECTION and not self.already_moving:
            self.game.update(self.DIRECTION[event.keysym])
            self.key_pressed = event.keysym
            self.already_moving = True
            print("PRESSED")

    def key_release(self, event):
        if event.keysym == self.key_pressed:
            self.key_pressed = None
            self.already_moving = False
            self.game.stop_updating()
            print("RELEASED")
        elif event.keysym == "Return":
            self.game.interaction()