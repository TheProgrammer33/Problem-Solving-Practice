"""
In this problem you will process two lists of numbers and return the difference.
The difference are numbers that appear in one of the lists but not both.
"""

def theDifference():
    firstList = input("Enter first set of data separated by space: ").split(" ")
    secondList = input("Enter second set of data separated by space: ").split(" ")
    differenceList = []

    for item in firstList:
        if item not in secondList:
            differenceList.append(int(item))
    
    for item in secondList:
        if item not in firstList:
            differenceList.append(int(item))

    if (len(differenceList)):
        listString = ""
        differenceList.sort()
        for item in differenceList:
            listString += str(item) + " "
        print(listString)
    else:
        print("No differences")