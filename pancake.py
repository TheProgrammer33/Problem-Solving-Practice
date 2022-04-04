
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
    print(pancakeSort(data))

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

def pancakeSort(arr):
    numberOfFlips = 0
    for i in range(len(arr)):
        newArray = arr[:len(arr)-(numberOfFlips)]
        largest = findLargest(newArray)
        arr = flip(arr, getPancakePosition(largest, arr))
        if (not arr[0][1]):
            arr = flip(arr, 0)
        arr = flip(arr, len(arr)-(numberOfFlips+1))
        numberOfFlips += 1
    return arr

def findLargest(arr):
    largest = 0
    for n in arr:
        if n[0] > largest:
            largest = n[0]
    return largest

def flip(arr, position):
    newArray = []
    for a in range(position, -1, -1):
        arr[a][1] = 0 if arr[a][1] else 1
        newArray.append(arr[a])
    for a in range(position+1, len(arr)):
        newArray.append(arr[a])
    return newArray

def getPancakePosition(largest, arr):
    for a in arr:
        if (a[0] == largest):
            return arr.index(a)