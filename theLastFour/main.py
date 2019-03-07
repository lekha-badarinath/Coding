#script to perform the actual simulation (object of the defined classes)
from theLastFour.theGame import Game
from theLastFour.teamDetails import Team

if __name__ == '__main__':
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

#     teamName2 = "ABC"
#     players2 = ["A","B","C","D"]
#     game2 = Team(teamName2,players2,probabilities)
#     play1 = Game(overs,target,game2)
#     play1.playing()