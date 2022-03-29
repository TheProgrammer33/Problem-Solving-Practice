import math

"""
What is the smallest positive integer whose square ends in the digits babbageNumber?
"""

def babbage(babbageNum, endDigits):
    endDigitsString = str(endDigits)
    for num in range(endDigits, pow(babbageNum, 2), pow(10, len(endDigitsString))):
        possibleAnswer = math.floor(math.sqrt(num))
        if (str(num)[-len(endDigitsString):] == endDigitsString and pow(possibleAnswer, 2) == num):
            return possibleAnswer

    return babbageNum