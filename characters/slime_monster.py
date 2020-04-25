import characters.monster as monster



class Slime(monster.Monster):

    def __init__(self, controler, view, name):
        super().__init__(controler, view, name)

    def delete(self):
        super().delete()
        update = ["slime", 1]
        self.controler.update_mission(update)
