

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
    winsLossCount = [0, 0]
    for i in range(possibilities):
        possibleOutcome = str(bin(i))[2:]
        game = "0"*(maxGamesLeft - len(possibleOutcome)) + possibleOutcome
        if (isWin(score.copy(), game)):
            winsLossCount[0] += 1
        else:
            winsLossCount[1] += 1
    
    probability = round(winsLossCount[0]/possibilities * 100, 6)
    return probability

def isWin(score, game):
    for result in range(len(game)):
        if game[result] == "1":
            score[0] += 1
        else:
            score[1] += 1
        if score[0] == 10:
            return True
        elif score[1] == 10:
            return False
    
