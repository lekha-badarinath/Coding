#takes data from the Team() class and populates the self.playing list
#and sends it to the Game() class as a list of players playing on the crease 
class ActivePlayers():
    def __init__(self,players):
        self.players = players
        self.playing = [self.players[0],self.players[1]]
        self.players.pop(0)
        self.players.pop(0)