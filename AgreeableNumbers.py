
"""
In this problem, agreeable numbers are two different numbers where the sum of the divisors 
of one number are equal to the other number. 
Given two numbers X and Y, the divisors of X sum to Y and the divisors of Y sum to X.
A divisor of a number is a positive factor of that number other than the number itself.
In other words, a number N is a divisor of X, if dividing X by N leaves no reminder.
The smallest pair of agreeable numbers is (220, 284).
They are agreeable because the divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110,
which sum to 284 and the divisors of 284 are 1, 2, 4, 71 and 142,
which sum to 220. You will be given two integer numbers and must determine if these are agreeable numbers.
"""

def agreeableNumbers():
    numbers = input("Enter two numbers separated by a space: ").split()

    for num in range(len(numbers)):
        number = int(numbers[num])
        finalNumber = 0
        for i in range(1, round(number/2)+1):
            if (number % i == 0):
                finalNumber += i
    
        if (finalNumber != int(numbers[0 if num else 1])):
            print("Not agreeable numbers")
            return
    
    print("Agreeable numbers")