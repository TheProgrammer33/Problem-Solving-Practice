import math

"""
Add (insert) the mathematical operators + or ─ (plus or minus) before
any of the digits in the decimal numeric string 123456789 such that
the resulting mathematical expression adds up to a particular sum (in this iconic case, 100).
"""

def sumTo(num):
    numbersString = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    signs = ['+', '-']
    for i in range(2):    
        for j in range(pow(2, 9)):
            answerToEquation = int(numbersString[0])
            equation = ""
            for k in range(j+1):
                equation += numbersString[j] + signs[i]

# no idea how to do this

    