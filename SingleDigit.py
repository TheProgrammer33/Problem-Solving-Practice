"""
In this problem you will start with a single positive number.
Subtract adjacent pairs of digits in that number to get the absolute value of their difference.
Each result is used to generate a new number.
Repeat that process as many times as necessary to arrive at a number that is a single digit.
Display the final single digit.
"""

def singleDigit():
    number = input("Enter the number: ")

    if (len(number) == 1):
        print(number)
    else:  
        while (True):
            newNumber = ""
            for i in range(len(number)-1):
                newNumber += str(abs((int(number[i]) - int(number[i+1]))))
            
            if (len(newNumber) == 1):
                print(newNumber)
                break
            
            number = str(int(newNumber))