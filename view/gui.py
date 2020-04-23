import tkinter as tk


class View(tk.Canvas):
    WIDTH = 1100
    HEIGHT = 650

    def __init__(self, master):
        super().__init__(master=master, width=self.WIDTH, height=self.HEIGHT, bg="black")
        self.reference = []
        # photoImage = tk.PhotoImage(file="characters/main_character.png")
        # self.player_canvas = self.create_image(500, 300, image=photoImage)
        # self.reference.append(photoImage)
        self.npcs = []
        self.grid()

        self.moving = None

    def initialise_game(self, npcs, player):
        image = tk.PhotoImage(file="maps/road.png") # TO DO --> mettre le chemin en paramètre pour les différentes maps
        self.create_image(self.WIDTH/2, self.HEIGHT, image=image, anchor="s", tag="move")
        self.reference.append(image)
        left = self.WIDTH/2 - 1240
        right = self.WIDTH/2 + 1240
        top = self.HEIGHT - 3508
        bottom = self.HEIGHT
        self.create_line(left, top, right, top, fill="white", tag="move")

        self.create_line(left,bottom, right, bottom, fill="white", tag="move")
        self.create_line(left, top, left, bottom, fill="white", tag="move")
        self.create_line(right, top, right, bottom, fill="white", tag="move")
        print("MAP CREATED")

        self.create_oval(player.position.x1, player.position.y1,
                         player.position.x2, player.position.y2, fill="black", tag="player")

        for npc in npcs:
            npc_canvas = self.create_oval(npc.position.x1, npc.position.y1,
                                          npc.position.x2, npc.position.y2,
                                          fill="Skyblue", tag=("move", "npc"))
            self.npcs.append(npc_canvas)

    def display_conversation(self, npc):
        self.create_rectangle(0, self.HEIGHT - self.HEIGHT/5, self.WIDTH, self.HEIGHT,
                              fill="white", tag="blank_for_text")
        self.write_conversation(npc)

    def write_conversation(self, npc, msg_number=0, index=0):
        self.delete("text")
        msg = npc.get_msg(msg_number)[:index]
        self.create_text(self.WIDTH/10, self.HEIGHT - self.HEIGHT/10, text=msg,
                         font=("arial", 10), tag="text", anchor="w")
        if index < len(npc.get_msg(msg_number)):
            self.master.after(5, lambda: self.write_conversation(npc, msg_number, index + 1))
        else:
            self.bind("<1>", lambda _: self.is_more_text(npc, msg_number))

    def is_more_text(self, npc, msg_number):
        print(len(npc.msgs), msg_number)
        if len(npc.msgs) - 1 > msg_number:
            self.write_conversation(npc, msg_number=msg_number+1)
            self.unbind("<1>")
        else:
            self.stop_conversation(npc)

    def stop_conversation(self, npc):
        self.delete("text")
        self.delete("blank_for_text")
        npc.already_conversing = False
        self.unbind("<1>")

    def update_view(self, x, y):
        """
        Moves the map so there is an illusion that it is the character that is currently moving.
        """
        self.move("move", x, y)
