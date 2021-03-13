import numpy as np

from shipInit import shipTypeList, shipList, boardSize, gameBoard

def verticalCheck(w, algorithmGrid, gameBoard):
	boatSize = w - 1
	for x in range(boardSize):
		for y in range(boardSize - boatSize):
			print(x, y)
			if 1 not in gameBoard[y:y+boatSize+1][x]:
				algorithmGrid[y:y+boatSize+1][x] += 1
	return algorithmGrid

def horizontalCheck(w, algorithmGrid, gameBoard):
	boatSize = w - 1
	for y in range(boardSize):
		for x in range(boardSize - boatSize):
			if 1 not in gameBoard[y][x:x+boatSize+1]:
				algorithmGrid[y][x:x+boatSize+1] += 1
	return algorithmGrid

def hunt(gameBoard, boardSize):
	algorithmGrid = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
	for w in shipTypeList:
		algorithmGrid = horizontalCheck(w, algorithmGrid, gameBoard)
		#algorithmGrid = verticalCheck(w, algorithmGrid, gameBoard)
	return algorithmGrid

test = hunt(gameBoard, boardSize)

for row in test:
	print(row)

for ship in shipList:
	for coord in ship:
		i, j = coord
		gameBoard[i][j] = 1

for row in gameBoard:
	print(row)
print()
test = hunt(gameBoard, boardSize)

for row in test:
	print(row)