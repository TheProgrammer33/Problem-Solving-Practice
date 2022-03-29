

"""
Given a number of points best of 19, return the probability that person 1 wins

input:
10 0
5 2
0 9
"""

def coinGame():
    score = input().split()
    score[0] = int(score[0])
    score[1] = int(score[1])
    maxGamesLeft = 19 - (score[0] + score[1])
    possibilities = pow(2, maxGamesLeft)
    game = "0"*maxGamesLeft
    games = [game]
    for i in range(possibilities):
        game[0] = 1 if (True) else (game[0] = 0)
        

def isWin(score, game):
    for result in range(game):
        if 
        if score[0] == 10:
            return True
        elif score[1] == 10:
            return False
    
