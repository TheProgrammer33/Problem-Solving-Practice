

"""
In short, instead of individual elements being sorted, the only operation allowed is to "flip" one end of the list
"""
def pancakeSort(arr):
    numberOfFlips = 0
    for i in range(len(arr)):
        newArray = arr[:len(arr)-(numberOfFlips)]
        largest = findLargest(newArray)
        arr = flip(arr, arr.index(largest))
        arr = flip(arr, len(arr)-(numberOfFlips+1))
        numberOfFlips += 1
    return arr

def findLargest(arr):
    largest = 0
    for n in arr:
        if n > largest:
            largest = n
    return largest

def flip(arr, position):
    newArray = []
    for a in range(position, -1, -1):
        newArray.append(arr[a])
    for a in range(position+1, len(arr)):
        newArray.append(arr[a])
    return newArray
