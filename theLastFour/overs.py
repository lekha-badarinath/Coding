#takes data from the Game() class and...
#1. populates the score board with the runs scored and balls used by batsman
#2. changes the player position if the run hit is 1,3 or 5
#3. removes the player from the activePlayers list and the playing list if he gets out


class Runs():
    def __init__(self,run,playing,remaining,scoreBoard,total,currentScore,target):
        self.run = run
        self.playing = playing
        self.remaining = remaining
        self.scoreBoard = scoreBoard
        self.total = total
        self.currentScore = currentScore
        self.target = target
        self.scoreBoard[self.playing[0]][1] += 1
        
        if self.run in [1,2,3,4,5,6]:
            self.scoreBoard[self.playing[0]][0] += self.run
            self.total += self.run
            self.currentScore -= self.run
            
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

