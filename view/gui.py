import tkinter as tk
import characters.Player as player


class View(tk.Canvas):

    DIRECTION = {"west": (6, 0),
                 "south": (0, -6),
                 "east": (-6, 0),
                 "north": (0, 6)}

    def __init__(self, master):
        super().__init__(master=master, width=500, height=500, bg="Skyblue")
        self.player = player.Player(self, "Cocograal", 1000, None)

        self.map = []
        self.create_map()
        photoImage = tk.PhotoImage(file="characters/character.png")
        self.player_canvas = self.create_image(250, 250, image=photoImage)
        self.map.append(photoImage)
        self.grid()

        self.moving = None

    def create_map(self):
        image = tk.PhotoImage(file="maps/road.png") # TO DO --> mettre le chemin en paramètre pour les différentes maps
        self.create_image(0, 0, image=image, tag="map")
        self.map.append(image)
        print("BONJOUR")

    def update_map(self, direction):
        print(direction)
        move_x, move_y = self.DIRECTION[direction]
        print(move_x, move_y)
        self.move("map", move_x, move_y)
        self.moving = self.master.after(75, lambda: self.update_map(direction))

    def stop_updating_map(self):
        self.master.after_cancel(self.moving)