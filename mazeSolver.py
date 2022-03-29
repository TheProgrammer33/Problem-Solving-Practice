

"""
Solve a maze given:
10 11
#.########
#....#...#
####.###.#
#........#
#.########
#.#...#..#
#.#.####.#
#.#......#
#.###.####
#.......*#
##########

print Yes if the maze is possible
"""

def mazeSolver():
    mazeDimensions = input().split()

    maze = []
    for i in range(int(mazeDimensions[1])):
        maze.append(input())
    
    position = findStartingPosition(maze)
    previousPosition = position
    checkpoints = []
    while (True):
        if (checkForExit(maze, position)):
            print("Yes")
            break
        surroundingPaths = getSurroundingPaths(maze, position, previousPosition)
        if (surroundingPaths.count(0) < 3):
            checkpoints.append({"Paths": surroundingPaths, "Position": position, "takenPaths": [getPreviousPathNumber(position, previousPosition)]})
            previousPosition = position
            position = getNextPath(surroundingPaths,checkpoints[-1]["takenPaths"])
        elif (surroundingPaths.count(0) == 3):
            previousPosition = position
            position = getNextPath(surroundingPaths, [])
        
        if ((position == -1 or surroundingPaths.count(0) == 4) and not checkForExit(maze, position)):
            if (len(checkpoints)):
                position = getNextPath(checkpoints[-1]["Paths"], checkpoints[-1]["takenPaths"])
                while position == -1 and len(checkpoints):
                    checkpoints.pop(-1)
                    if len(checkpoints):
                        position = getNextPath(checkpoints[-1]["Paths"], checkpoints[-1]["takenPaths"])
                if (position != -1):
                    previousPosition = checkpoints[-1]["Position"]
            else:
                print("No")
                break

def getNextPath(paths, takenPaths):
    for i in range(len(paths)):
        if paths[i] != 0 and i not in takenPaths:
            takenPaths.append(i)
            return paths[i]
    return -1
    

def getSurroundingPaths(maze, position, previousPosition):
    path = [0,0,0,0]
    try:
        north = [position[0]-1, position[1]]
        south = [position[0]+1, position[1]]
        east = [position[0], position[1]-1]
        west = [position[0], position[1]+1]
        if (maze[north[0]][north[1]] == "." and north != previousPosition):
            path[0] = north
        if (maze[south[0]][south[1]] == "." and south != previousPosition):
            path[1] = south
        if (maze[east[0]][east[1]] == "." and east != previousPosition):
            path[2] = east
        if (maze[west[0]][west[1]] == "." and west != previousPosition):
            path[3] = west
    except:
        pass
    return path

def getPreviousPathNumber(position, previousPosition):
    north = [position[0]-1, position[1]]
    south = [position[0]+1, position[1]]
    east = [position[0], position[1]-1]
    west = [position[0], position[1]+1]
    if (north == previousPosition):
        return 0
    if (south == previousPosition):
        return 1
    if (east == previousPosition):
        return 2
    if (west == previousPosition):
        return 3


def findStartingPosition(maze):
    if (maze[0].find(".") != -1):
        return [0, maze[0].find(".")]
    elif (maze[len(maze)-1].find(".") != -1):
        return [0, maze[len(maze)-1].find(".")]
    for i in range(len(maze)):
        if (maze[i][0] == "."):
            return [i, 0]
        elif (maze[i][len(maze[i])-1] == "."):
            return [i, len(maze[i])-1]

def checkForExit(maze, position):
    if position == None and maze[0][0] == "*":
        return True
    try:
        north = [position[0]-1, position[1]]
        south = [position[0]+1, position[1]]
        east = [position[0], position[1]-1]
        west = [position[0], position[1]+1]
        if (maze[north[0]][north[1]] == "*" or maze[south[0]][south[1]] == "*" or maze[east[0]][east[1]] == "*" or maze[west[0]][west[1]] == "*"):
            return True
    except:
        pass
    return False