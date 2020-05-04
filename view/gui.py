import tkinter as tk
import util.vector as vector


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
        self.grid(row=0, column=0, columnspan=2)
        self.borders = vector.Vector2f(self.WIDTH/2 - 1240, self.HEIGHT - 3508, self.WIDTH/2 + 1240, self.HEIGHT)
        self.moving = None
        self.menu = False

    def initialise_game(self, npcs, player):
        image = tk.PhotoImage(file="maps/road.png") # TO DO --> mettre le chemin en paramètre pour les différentes maps
        self.create_image(self.WIDTH/2, self.HEIGHT, image=image, anchor="s", tag="move")
        self.reference.append(image)
        self.create_line(self.borders.x1, self.borders.y1, self.borders.x2, self.borders.y1, fill="white", tag="move")

        self.create_line(self.borders.x1, self.borders.y2, self.borders.x2, self.borders.y2, fill="white", tag="move")
        self.create_line(self.borders.x1, self.borders.y1, self.borders.x1, self.borders.y2, fill="white", tag="move")
        self.create_line(self.borders.x2, self.borders.y1, self.borders.x2, self.borders.y2, fill="white", tag="move")
        print("MAP CREATED")

        self.create_oval(player.position.x1, player.position.y1,
                         player.position.x2, player.position.y2, fill="black", tag="player")

        for npc in npcs:
            npc_canvas = self.create_oval(npc.position.x1, npc.position.y1,
                                          npc.position.x2, npc.position.y2,
                                          fill="Skyblue", tag=("move", "npc"))
            self.npcs.append(npc_canvas)

    def initialise_monsters(self, position):
        self.create_oval(position.x1, position.y1, position.x2, position.y2, fill="white", tag=("monster", "move"))

    def open_menu(self, master):
        self.menu = True
        self.create_rectangle(self.WIDTH/4, self.HEIGHT/4, self.WIDTH*3/4, self.HEIGHT*3/4, fill="black", tag="menu")
        entry = tk.Entry(self)
        self.create_window(self.WIDTH/2, self.HEIGHT/3, window=entry, tag="menu")
        btn = tk.Button(self, text="close menu")
        self.create_window(self.WIDTH/2, self.HEIGHT/2, window=btn, tag="menu")
        btn.bind("<1>", lambda _: self.delete("menu"))
        self.master.bind("<Return>", lambda _: self.master.get_entry_text(entry.get()))

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

    def delete_object(self, position):
        widgets_at_position = self.find_overlapping(position.x1, position.y1, position.x2, position.y2)
        self.delete(widgets_at_position[-1])

    def update_view(self, x, y):
        """
        Moves the map so there is an illusion that it is the character that is currently moving.
        """
        self.move("move", x, y)
        self.borders += vector.Vector2f(x, y, x, y)
