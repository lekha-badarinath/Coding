import random      

class ProbabilityBoard():
    
    def __init__(self,players,probabilities = []):
        self.players = players
        self.probabilities = probabilities
        self.probTable = {x:y for (x,y) in zip(self.players,self.probabilities)}
        
class ScoreBoard():
    def __init__(self,players):
        self.players = players
        self.scoreBoard = {}
        for player in self.players:
            self.scoreBoard[player] = [0,0]
       
class ActivePlayers():
    def __init__(self,players):
        self.players = players
        self.playing = [self.players[0],self.players[1]]
        self.players.pop(0)
        self.players.pop(0)

class MatchCommentary():
    def __init__(self,count,ball,batsman,run):
        self.count = count
        self.ball = ball+1
        self.batsman = batsman
        self.run = run
    
    def printCommentary(self):
        if type(self.run) is not str:
            if self.run == 1:
                print ("%d.%d %s scores %d run" %(self.count, self.ball, self.batsman, self.run))
            else:
                print ("%d.%d %s scores %d run" %(self.count, self.ball,self. batsman, self.run))
        else:
            print ("%d.%d %s %s" %(self.count, self.ball, self.batsman, self.run))

class MatchSummary():
    def __init__(self,teamName,scoreBoard,total,target):
        self.teamName = teamName
        self.scoreBoard = scoreBoard
        self.total = total
        self.target = target
    
    def printSummary(self):
        print ("*"*50)
        if self.total == self.target:
            print ("It's a tie!")
        elif self.total < self.target:
            print ("%s lost by %d runs" %(self.teamName,self.target-self.total))
        elif self.total > self.target:
            print ("%s won by %d runs" %(self.teamName,self.total-self.target))
        print ("*"*50)
        
        print ("%s scored - %s runs" %(self.teamName,self.total))
        for scores in self.scoreBoard:
            print ("%s - %d (%d balls)" %(scores, self.scoreBoard[scores][0], self.scoreBoard[scores][1]))     

class Runs():
    def __init__(self,run,playing,remaining,scoreBoard):
        self.run = run
        self.playing = playing
        self.remaining = remaining
        self.scoreBoard = scoreBoard
        self.scoreBoard[self.playing[0]][1] += 1
        if self.run in [1,2,3,4,5,6]:
            self.scoreBoard[self.playing[0]][0] += self.run
            
            if self.run in [1,3,5]:
                self.playing = self.playing[::-1]
                

        if self.run == "Out":
            if len(self.remaining) != 0:
                self.scoreBoard[self.playing[0]][1] -= 1
                self.playing.pop(0)
                self.playing.insert(0, self.remaining[0])
                self.remaining.pop(0)
            else:
                self.playing.pop(0)
                  

class Team():   
    
    def __init__(self,teamName,players,probabilities):
        self.teamName = teamName
        self.players = players
        self.probabilities = probabilities
        self.probBoard = ProbabilityBoard(self.players,self.probabilities)
        self.score_board = ScoreBoard(self.players)
        self.activePlayers = ActivePlayers(players)

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
                    if run in [1,2,3,4,5,6]:
                        self.total += run
                        self.currentScore -= run
                    updates = MatchCommentary(count,ball,playing[0],run)
                    updates.printCommentary()
                    runs = Runs(run,playing,remaining,scoreBoard)
                    playing = runs.playing
                    remaining = runs.remaining
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
            
            


teamName = "Lengaburu"
players = ["Kirat Boli","N.S Nodhi","R Rumrah","Shashi Henra"]
probabilities = [[5,    30,    25,    10,    15,    1,    9,    5],
                 [10,    40,    20,    5,    10,    1,    4,    10],
                 [20,    30,    15,    5,    5,    1,    4,    20],
                 [30,    25,    5,    0,    5,    1,    4,    30]]    

game = Team(teamName,players,probabilities)

overs = 4
target = 40
play = Game(overs,target,game)
play.playing()