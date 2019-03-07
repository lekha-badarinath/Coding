#Creates a dictionary which generates the score board with 
#details of runs scored and balls used
#Each time a valid run is made (1,2,3,4,5,6) by the player,
#the score board gets updated
#self.scoreBoard is sent to the MatchSummary() class for displaying the results
class ScoreBoard():
    def __init__(self,players):
        self.players = players
        self.scoreBoard = {}
        for player in self.players:
            self.scoreBoard[player] = [0,0]