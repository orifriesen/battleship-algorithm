import numpy as np

from numpy import unravel_index
from shipInit import *

def verticalCheck(w, algorithmGrid, gameBoard):
	boatSize = w - 1
	for x in range(boardSize):
		for y in range(boardSize - boatSize):
			hitAlready = False
			for z in range(boatSize+1):
				if gameBoard[y+z][x] == 1:
					hitAlready = True
			if hitAlready == False:
				for z in range(boatSize+1):
					algorithmGrid[y+z][x] += 1
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
		algorithmGrid = verticalCheck(w, algorithmGrid, gameBoard)
	return algorithmGrid

def findNextPossibleHits(targetHits, targetMisses):
	possibleNextHits = []
	for x in range(boardSize):
		for y in range(boardSize):
			if targetHits[x][y] == 1:
				if x > 0 and targetHits[x-1][y] != 1 and targetMisses[x-1][y] != 1:
					possibleNextHits.append((x-1, y))
				if x + 1 < boardSize and targetHits[x+1][y] != 1 and targetMisses[x+1][y] != 1:
					possibleNextHits.append((x+1, y))
				if y > 0 and targetHits[x][y-1] != 1 and targetMisses[x][y-1] != 1:
					possibleNextHits.append((x, y-1))
				if y + 1 < boardSize and targetHits[x][y+1] != 1 and targetMisses[x][y-1] != 1:
					possibleNextHits.append((x, y+1))
	return possibleNextHits
			

def target(firstHit):
	targetHits = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
	targetMisses = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
	targetHits[firstHit] = 1
	return findNextPossibleHits(targetHits, targetMisses)

def sunkShipTest(targetHits):
	if set(any(x in shipList)).issubset (set(targetHits)):
		return True
	else:
		return False

def allShipSunk(gameBoard, hits, boardSize):
	sunk = True
	for y in range(boardSize):
		for x in range(boardSize):
			if shipsOnGameBoard[x][y] == 1 and hits[x][y] != 1:
				sunk = False
	if sunk == False:
		return False
	else:
		return True

#for ship in shipList:
#	for coord in ship:
#		i, j = coord
#		gameBoard[i][j] = 1

#while allShipSunk() is False:
for x in range(25):
	algorithm = hunt(gameBoard, boardSize)
	nextTest = unravel_index(algorithm.argmax(), algorithm.shape)
	gameBoard[nextTest] = 1
	#print(algorithm)
	print(nextTest)
	#print(gameBoard)
	if any(nextTest in y for y in shipList):
		print("hit!!!!")
		hits[nextTest] = 1
		print(target(nextTest))

	print(allShipSunk(gameBoard, hits, boardSize))