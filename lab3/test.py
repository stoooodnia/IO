import numpy as np
# 0 - wall, 1 - empty path, 2 - start, 3 - exit
labyrinth = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                      [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
                      [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
                      [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
                      [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 3, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# definiujemy parametry chromosomu
# geny to kierunek ruchu 0-prawo 1-lewo 2-góra 3-dół
gene_space = [0, 1, 2, 3]


def findStartPoint(nparray):
    return list(zip(*np.where(nparray == 2)))[0]


def findExitPoint(nparray):
    return list(zip(*np.where(nparray == 3)))[0]


def fitness_func():
    startPoint = [0, 0]
    startPoint[0] = findStartPoint(labyrinth)[0]
    startPoint[1] = findStartPoint(labyrinth)[1]  # type: ignore

    exitPoint = [0, 0]
    exitPoint[0] = findExitPoint(labyrinth)[0]  # type: ignore
    exitPoint[1] = findExitPoint(labyrinth)[1]  # type: ignore


def getDistance(presentPlace, exitPoint):
    aSquare = (presentPlace[0] - exitPoint[0]) ** 2
    bSquare = (presentPlace[1] - exitPoint[1]) ** 2
    return np.sqrt(aSquare + bSquare)

# iterate over chromosome to get index of presentPlace after moves from startPoint


def computeMoves(startPoint, solution):
    presentPlace = startPoint
    # 0 - right, 1 - left, 2 - up, 3 - down
    for i in solution:
        if i == 0:
            if labyrinth[presentPlace[0], presentPlace[1] + 1] == 0:
                pass
            else:
                presentPlace[1] += 1
        elif i == 1:
            if labyrinth[presentPlace[0], presentPlace[1] - 1] == 0:
                pass
            else:
                presentPlace[1] -= 1
        elif i == 2:
            if labyrinth[presentPlace[0] - 1, presentPlace[1]] == 0:
                pass
            else:
                presentPlace[0] -= 1
        elif i == 3:
            if labyrinth[presentPlace[0] + 1, presentPlace[1]] == 0:
                pass
            else:
                presentPlace[0] += 1
    return presentPlace
