
"""
Given a stack of Pancakes with varying sizes, assume one side of every pancake is burned.
Develop code to flip pancakes so that the largest pancakes are on the bottom and the burned sides are face down.
To flip a pancake you find a pancake and flip everything above that pancake.
Example data:
[[1, 0], [7, 0],  [9, 1],  [10, 0],  [6, 1],  [4, 1],  [8, 0],  [3, 0],  [5, 1],  [2, 1]]
"""
def pancakeProblem():
    data = randomPancakeDataGenerator()
    print(data)
    print(sortPancakes(data))
    print(data)

def randomPancakeDataGenerator():
    import random
    data = []
    listOfNumbers = []
    listLength = random.randint(5, 10)
    for num in range(listLength):
        listOfNumbers.append(num)
        data.append([])
    for i in range(listLength):
        index = listOfNumbers.pop(random.randint(0, len(listOfNumbers)-1))
        burnedSideUp = random.randint(0, 1)
        data[index] = [i, burnedSideUp]
    return data

def flipPancakes(allPancakes, numOfPancakes):
    stack = allPancakes[:numOfPancakes]
    flippedStack = []
    for pancake in stack:
        p = 0 if pancake[1] else 1
        flippedStack.insert(0, [pancake[0] , p])
    allPancakes[:numOfPancakes] = flippedStack
    return allPancakes

def sortPancakes(pancakeStack):
    bottomPosition = len(pancakeStack)-1
    previousLargestIndex = -1
    while (not stackChecker(pancakeStack)):
        index = findNextLargestPancake(pancakeStack, previousLargestIndex)
        pancakeStack = flipPancakes(pancakeStack, index+1)
        if (not pancakeStack[0][1]):
            pancakeStack = flipPancakes(pancakeStack, 1)
        pancakeStack = flipPancakes(pancakeStack, bottomPosition+1)        

        previousLargestIndex = index
        bottomPosition -= 1
    return pancakeStack

def findNextLargestPancake(stack, previousLargest):
    largestPancakeIndex = (len(stack)-1)*-1
    numbers = []
    for i in stack:
        numbers.append(i[0])
    

    for pancake in range(len(stack)):
        if stack[pancake][0] > stack[largestPancakeIndex][0] and stack[pancake][0] < stack[previousLargest][0]:
            largestPancakeIndex = pancake
    if (largestPancakeIndex < 0):
        # value_if_true if condition else value_if_false
        largestPancakeIndex = previousLargest if previousLargest != -1 else len(stack)-1
    return largestPancakeIndex

# def findOutOfPlace(stack):
#     for pancake in reversed(stack):
#         if 

# def isLargestInStack(stack, ):


def stackChecker(pancakes):
    for p in range(len(pancakes)-2):
        if pancakes[p][0] > pancakes[p+1][0]:
            return False
        if pancakes[p][1]:
            return False
    return True

