#class used to print the final summary of the match
#along with details on whether the team won or lost
#takes data from Game() class
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