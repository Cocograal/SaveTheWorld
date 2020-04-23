import characters.main_character as main_character
import characters.NPC as npc
import util.vector as vector


class Game():

    NPC_TRAITS = {1: "Jack, 50, slime, 600, 305, 640, 345"}

    DIRECTION = {"west": (6, 0),
                 "south": (0, -6),
                 "east": (-6, 0),
                 "north": (0, 6)}

    def __init__(self, master, view):
        self.master = master
        self.view = view
        self.npcs = self.initialise_npc()
        self.player = main_character.MainCharacter(self, self.view, "characters/players.txt")

        self.view.initialise_game(self.npcs, self.player)
        self.moving = None

    def initialise_npc(self):
        npcs = []
        with open("characters/npc_traits.txt") as file:
            data = file.read()
        data_per_line = data.split("\n")
        for npc_link in data_per_line:
            npc_initialised = npc.Npc(self, self.view, npc_link)
            npcs.append(npc_initialised)
        return npcs

    def interaction(self):
        for npc in self.npcs:
            if npc.is_player_around() and not npc.already_conversing:
                npc.converse()
                break

    def update(self, direction):
        move_x, move_y = self.DIRECTION[direction]
        arrival = self.view.find_overlapping(self.player.position.x1 - move_x, self.player.position.y1 - move_y,
                                             self.player.position.x2 - move_x, self.player.position.y2 - move_y)
        print(len(arrival))

        if len(arrival) < 3:
            self.view.update_view(move_x, move_y)
            for npc in self.npcs:
                npc.update_position(direction)
            print(npc.position)
        self.moving = self.master.after(2, lambda: self.update(direction))

    def stop_updating(self):
        self.master.after_cancel(self.moving)
