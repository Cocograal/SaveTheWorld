import tkinter as tk


class View(tk.Canvas):

    def __init__(self, master):
        super().__init__(master=master, width=1100, height=650, bg="Skyblue")
        self.reference = []
        # photoImage = tk.PhotoImage(file="characters/main_character.png")
        # self.player_canvas = self.create_image(500, 300, image=photoImage)
        # self.reference.append(photoImage)
        self.npcs = []
        self.grid()

        self.moving = None

    def initialise_game(self, npcs, player):
        image = tk.PhotoImage(file="maps/road.png") # TO DO --> mettre le chemin en paramètre pour les différentes maps
        self.create_image(0, 800, image=image, anchor="s", tag="move")
        self.reference.append(image)
        print("MAP CREATED")

        self.create_oval(player.position.x1, player.position.y1,
                         player.position.x2, player.position.y2, fill="black", tag="player")

        for npc in npcs:
            npc_canvas = self.create_oval(npc.position.x1, npc.position.y1,
                                          npc.position.x2, npc.position.y2,
                                          fill="Skyblue", tag=("move", "npc"))
            self.npcs.append(npc_canvas)

    def update_view(self, x, y):
        """
        Moves the map so there is an illusion that it is the character that is currently moving.
        """
        self.move("move", x, y)
