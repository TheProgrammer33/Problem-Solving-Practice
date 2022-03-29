

"""
Given a certain number of blocks what is are the three dimensions of the smallest box that can perfectly hold the blocks.
The box cannot have any empty spaces, and must use the least material possible.
"""

import math

def blocks():
    numberOfBlocks = int(input())
    
    bestSurfaceArea = getBoxSurfaceArea(1, 1, numberOfBlocks)
    boxDimensions = "1 1 " + str(numberOfBlocks)
    for i in range(1, int(numberOfBlocks**(1/2))+1):
        for j in range(1, int(math.sqrt(numberOfBlocks))+1):
            thirdDimension = int(numberOfBlocks/(i*j))
            surfaceArea = getBoxSurfaceArea(i, j, thirdDimension)
            if (surfaceArea < bestSurfaceArea and (i*j*thirdDimension) == numberOfBlocks):
                bestSurfaceArea = surfaceArea
                boxDimensions = str(i) + " " + str(j) + " " + str(thirdDimension)
    
    return boxDimensions

def getBoxSurfaceArea(a, b, c):
    return a*b*2 + a*c*2 + b*c*2