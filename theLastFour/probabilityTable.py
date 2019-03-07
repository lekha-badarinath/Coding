#takes the player names and their score probability lists,
#prepares a dictionary which is used in the Game() class to simulate
#the run
class ProbabilityBoard():
    
    def __init__(self,players,probabilities = []):
        self.players = players
        self.probabilities = probabilities
        self.probTable = {x:y for (x,y) in zip(self.players,self.probabilities)}