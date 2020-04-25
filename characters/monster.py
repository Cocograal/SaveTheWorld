import random
import util.vector as vector


class Monster():

    DIRECTION = {"west": (6, 0),
                 "south": (0, -6),
                 "east": (-6, 0),
                 "north": (0, 6)}

    def __init__(self, controler, view, name):
        self.controler = controler
        self.view = view
        self.name = name
        self.position = self.randomise_position()
        self.view.initialise_monsters(self.position)
        print(f"{self.name} has been initialised")

    def __str__(self):
        return self.name

    def is_player_around(self):
        is_around = self.view.find_overlapping(self.position.x1 - 10, self.position.y1 - 10,
                                               self.position.x2 + 10, self.position.y2 + 10)
        print(is_around)
        if len(is_around) >= 3:
            return True
        return False

    def delete(self):
        self.view.delete_object(self.position)

    def randomise_position(self):
        corner_x1 = random.randrange(self.view.borders.x1, self.view.borders.x2)
        print(corner_x1)
        corner_x2 = corner_x1 + 40 if corner_x1 + 40 <= self.view.borders.x2 else corner_x1 - 40

        corner_y1 = random.randrange(self.view.borders.y1, self.view.borders.y2)
        corner_y2 = corner_y1 + 40 if corner_y1 + 40 < self.view.borders.y2 else corner_y1 - 40
        return vector.Vector2f(corner_x1, corner_y1, corner_x2, corner_y2)

    def update_position(self, direction):
        move_x, move_y = self.DIRECTION[direction]
        self.position += vector.Vector2f(move_x, move_y, move_x, move_y)