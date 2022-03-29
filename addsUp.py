"""
In this problem you will be given a target number and a list of numbers to search.
You will need to identify all pairs of numbers that sum to the target number.
For example, given the target number of 6 and the list of 16, 11, 2, 8, 6, 7, 4, 33, -2,
the pairs (2, 4) and (8, -2) sum to 6.
In addition to listing the pairs that sum to the target number,
you will need to list their position in the original list. The pair (2, 4) was located at 3 and 7.
The pair (8, -2) was located at 4 and 9.
"""

def addsUp():
    numbers = input("Enter the desired sum, number of elements, each element: ").split()
    target = numbers.pop(0)
    listLength = numbers.pop(0)
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if (int(numbers[i]) + int(numbers[j]) == int(target)):
                print("(" + numbers[i] + ", " + numbers[j] + ") found at [" + str(i+1) + "]" + "[" + str(j+1) + "]")
