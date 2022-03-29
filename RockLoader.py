import math

"""
The Rockland Quarry stores rocks in bags. 
The first bag on the shelf has 1 pound of rocks, the next bag has 2 pounds of rocks,
the next has 3 pounds of rocks and so on.
The quarry has an unlimited number of bags of rocks.
In other words, the heaviest bag stored weighs as much as the largest integer value.
A customer specifies a weight when ordering rocks. Rocky, the forklift operator,
always takes bags from adjacent locations to meet the required weight.
He also always takes a minimum of two bags.
You must write an application to help Rocky find all the possible
combinations of rock bags with consecutive weights that will total the weight the customer ordered.
For example, Bobby Stone has ordered 15 pounds of rock.
There are 3 combinations of consecutive weights that will add to 15.
"""
def rockLoader():
    weight = int(input("Enter weight of rock order: "))
    listOfSolutions = []
    for i in range(math.ceil(weight/2), 0, -1):
        solution = getPreviousNumberSum(i,weight)
        if (solution != -1 and solution[1] != i):
            listOfSolutions.append(solution)
            if (solution[1] == 1):
                break 

    outputSolution(listOfSolutions)

def getPreviousNumberSum(startingNumber, target):
    total = 0
    number = startingNumber
    iteration = 0
    while(total < target and number > 0):
        total += number
        iteration += 1
        if (total == target):
            return (iteration, number)
        number -= 1
    return -1

def outputSolution(solutions):
    total = 0
    for solution in solutions:
        total += solution[1] 
    print(str(len(solutions)) + " " + str(total))