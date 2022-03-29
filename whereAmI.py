"""
In this problem you will need to determine which quadrant a given point is in.
There are four quadrants, numbered from 1 to 4, as shown in the diagram below.
Given the X, Y coordinates of a point display 1, 2, 3, or 4 to indicate the quadrant in which the point is located.
"""

def whereAmI():
    quadrants = ["Q1", "Q2", "Q3", "Q4"]
    coordinates = input("Enter X and Y separated by a space: ").split(" ")
    coordinates[0] = int(coordinates[0])
    coordinates[1] = int(coordinates[1])

    if (coordinates[0] > 0):
        quadrants.pop(1)
        quadrants.pop(1)
    else:
        quadrants.pop(0)
        quadrants.pop(2)

    if (coordinates[1] > 0):
        quadrants.pop(1)
    else:
        quadrants.pop(0)

    print(quadrants[0])