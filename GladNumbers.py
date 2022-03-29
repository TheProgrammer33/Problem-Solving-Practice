"""
The Glad to be One number sequence are those whose sequence ends in a one.
Numbers that are not “glad” are those that infinitely repeat a sequence of numbers but never reach the number one.
For this problem you must determine if a number is a glad number or not.
For a given positive integer N, the next number in the sequence will be the sum of the squares of its digits.
Continue to generate numbers in the sequence until the sequence reaches one or the sequence begins to repeat itself.
The original input is a glad number if the sequence reaches one.
The original input is not a glad number if the sequence starts to repeat itself without reaching one.
"""

def GladNumbers(number=0):
    if (number):
        number = input("Enter a positive integer: ")
    notAnswered = True

    numberHistory = [int(number)]
    while (notAnswered):
        total = 0
        for i in range(len(number)):
            total += pow(int(number[i]), 2)
        
        if (total in numberHistory):
            print("Not a Glad Number")
            notAnswered = False
        elif (total == 1):
            print("Glad Number")
            notAnswered = False
        numberHistory.append(total)
        number = str(total)