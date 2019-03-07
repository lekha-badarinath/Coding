#takes data from Game() glass and displays it in the desired format
class MatchCommentary():
    def __init__(self,count,ball,player,run):
        self.count = count
        self.ball = ball+1
        self.player = player
        self.run = run
    
    def printCommentary(self):
        if type(self.run) is not str:
            if self.run == 1:
                print ("%d.%d %s scores %d run" %(self.count, self.ball, self.player, self.run))
            else:
                print ("%d.%d %s scores %d run" %(self.count, self.ball,self. player, self.run))
        else:
            print ("%d.%d %s %s" %(self.count, self.ball, self.player, self.run))