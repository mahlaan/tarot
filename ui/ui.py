from abc import ABCMeta

class UI(metaclass=ABCMeta):
    def requestNumRounds(self):
        pass

    def requestPlayers(self):
        pass