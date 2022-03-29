"""
How are duplicates removed from an array without using any library?
test data:
[1, 5, 3, 4, 1, 3, 8, 6, 7, 9, 1, 2, 11, 25, 5]
["test", "banana", "water", "test", "test", "watermelon", "theory", "code", "cod", "balloon"]
"""
def removeDuplicates(list):
    newList = []
    for item in list:
        if (not existsInList(newList, item)):
            newList.append(item)
    return newList

def existsInList(list, item):
    for i in list:
        if (i == item):
            return True
    return False
