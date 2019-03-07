#takes data from classes - ProbabilityBoard(), ScoreBoard() and ActivePlayers()
#takes user input data - team name, players' list and player probabilities
#populates the data and sends it to Game() class for the actual game
from theLastFour.probabilityTable import ProbabilityBoard
from theLastFour.scoreTable import ScoreBoard
from theLastFour.playersOnCrease import ActivePlayers

class Team():   
    
    def __init__(self,teamName,players,probabilities):
        self.teamName = teamName
        self.players = players
        self.probabilities = probabilities
        self.probBoard = ProbabilityBoard(self.players,self.probabilities)
        self.score_board = ScoreBoard(self.players)
        self.activePlayers = ActivePlayers(players)