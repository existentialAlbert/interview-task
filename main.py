from model.Player import Player


class Tamriel:
    __instance = None
    players = []

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Tamriel()
        return cls.__instance

    def addPlayer(self, player):
        if isinstance(player, Player):
            self.players.append(player)


if __name__ == '__main__':
    Tamriel = Tamriel()
    print("The Skyrim VII: ITMO University v0.0.1")
    protagonist = Player()
    Tamriel.addPlayer(protagonist)
    protagonist.start()
