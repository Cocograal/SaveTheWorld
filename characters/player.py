import util.vector as vector


class Player():

    def __init__(self, master, view, file_link):
        self.master = master
        self.view = view
        self.name, self.money, self.monsters, self.position, self.msgs = self.split_informations(file_link)

        print(f"{self} INITIALISED SUCCESSFULLY")

    def split_informations(self, file_link):
        with open(file_link) as file:
            infos = file.read()
        info_split = infos.split("; ")
        name = info_split[0]
        money = int(info_split[1])
        monster = info_split[2]
        position = vector.Vector2f(int(info_split[3]), int(info_split[4]), int(info_split[5]), int(info_split[6]))
        msgs = info_split[7].split("\n")
        msgs.remove("")
        return name, money, monster, position, msgs