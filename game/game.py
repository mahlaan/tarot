from numpy.random import randint

from .round import Round

class Game:
    # default number of rounds
    nDefaultRounds = 5

    """
    Initialise a game, a user interface will be used to communicate
    to the users.
    """
    def __init__(self, ui):
        # get the list of players as a list of instances of abc Player
        self.players = ui.requestPlayers()
        self.nPlayers = len(self.players)
        self.nRounds = ui.requestNumRounds(Game.nDefaultRounds)
        self.ui = ui

        self.startingPlayer = randint(0, self.nPlayers)

    def play(self):
        for _ in self.nRounds:
            round = Round(self.ui, self.players, self.startingPlayer)
            round.play()

            self.ui.displayScores()

            self.startingPlayer = (self.startingPlayer + 1) % self.nPlayers
