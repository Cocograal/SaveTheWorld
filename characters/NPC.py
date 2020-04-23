import characters.player as player
import util.vector as vector

class Npc(player.Player):

    DIRECTION = {"west": (6, 0),
                 "south": (0, -6),
                 "east": (-6, 0),
                 "north": (0, 6)}

    def __init__(self, master, view, npc_link):
        super().__init__(master, view, npc_link)
        self.already_conversing = False

    def __str__(self):
        return "NPC"

    def is_player_around(self):
        is_around = self.view.find_overlapping(self.position.x1 - 10, self.position.y1 - 10,
                                               self.position.x2 + 10, self.position.y2 + 10)
        if len(is_around) >= 3:
            return True
        return False

    def converse(self):
        self.already_conversing = True
        self.view.display_conversation(self)

    def get_msg(self, msg_number):
        msg = self.msgs[msg_number]
        return msg

    def update_position(self, direction):
        move_x, move_y = self.DIRECTION[direction]
        self.position += vector.Vector2f(move_x, move_y, move_x, move_y)
