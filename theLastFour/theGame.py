#takes data from Team and simulates the game
#takes data from classes - MatchCommentary(), Runs(), MatchSummary()
#and sends the needed information to these classes
import random
from theLastFour.commentary import MatchCommentary
from theLastFour.overs import Runs
from theLastFour.summary import MatchSummary
class Game():
    def __init__(self,overs,target=None, *teams):
        self.team = [team for team in teams]
        self.overs = overs
        self.target = target
        self.outcomes = ["Dot Ball",1,2,3,4,5,6,"Out"]
        self.currentScore = self.target

    def playing(self):
        for team in self.team:
            prob = team.probBoard.probTable  
            scoreBoard = team.score_board.scoreBoard
            activePlayers = team.activePlayers
            remaining = activePlayers.players
            playing = activePlayers.playing
            self.total = 0
            count = 0
            while self.overs > 0:
                print ("\n%d overs left. %d runs to win\n" %(self.overs,self.currentScore))
                for ball in range(0,6):
                    run = random.choices(self.outcomes,prob[playing[0]]) 
                    run = run[0] 
                    updates = MatchCommentary(count,ball,playing[0],run)
                    updates.printCommentary()
                    runs = Runs(run,playing,remaining,scoreBoard,self.total,self.currentScore,self.target)
                    playing = runs.playing
                    remaining = runs.remaining
                    self.total = runs.total
                    self.currentScore = runs.currentScore
                    if self.total > self.target:
                        break
                    if len(playing) == 1:
                        print ("All out")
                        break
                
                if len(playing) == 1:
                    break
                if self.total > self.target:
                    break
                
                playing = playing[::-1]
                
                count += 1
                self.overs -= 1
            
            summary = MatchSummary(team.teamName,scoreBoard,self.total,self.target)
            summary.printSummary()