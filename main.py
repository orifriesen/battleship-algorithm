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
				if y + 1 < boardSize and targetHits[x][y+1] != 1 and targetMisses[x][y+1] != 1:
					possibleNextHits.append((x, y+1))
	return possibleNextHits

def target(targetHits, algorithm, targetMisses):
	possibleNextHits = findNextPossibleHits(targetHits, targetMisses)
	global numberOfTurns

	for x in range(len(possibleNextHits)):
		possibleNextHits = findNextPossibleHits(targetHits, targetMisses)
		possibleArray = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
		for x in possibleNextHits:
			possibleArray[x] = algorithm[x]
		nextTest = unravel_index(possibleArray.argmax(), possibleArray.shape)
		print("next shot:", nextTest)
		if any(nextTest in y for y in shipList):
			print("hit!!!")
			numberOfTurns += 1
			print("turn:",  numberOfTurns)
			hits[nextTest] = 1
			targetHits[nextTest] = 1
			if sunkShipTest(targetHits):
				print("sunk ship!!!")
				return targetHits
			target(targetHits, algorithm, targetMisses)
			if sunkShipTest(targetHits):
				print("sunk ship!!!")
				return targetHits
		else:
			print("miss!!")
			numberOfTurns += 1
			print("turn:",  numberOfTurns)
			targetMisses[nextTest] = 1
			gameBoard[nextTest] = 1
		print()

def sunkShipTest(targetHits):
	targetCoordList = []
	for x in range(boardSize):
		for y in range(boardSize):
			if targetHits[x][y] == 1:
				targetCoordList.append((x, y))
	for x in shipList:
		list1 = targetHits.tolist()
		if x == targetCoordList:
			for c in range(len(shipTypeList) - 1):
				if shipTypeList[c] == len(x):
					del shipTypeList[c]
					break
			return True
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

while allShipSunk(gameBoard, hits, boardSize) is False:
	algorithm = hunt(gameBoard, boardSize)
	nextTest = unravel_index(algorithm.argmax(), algorithm.shape)
	print("next shot:", nextTest)
	if any(nextTest in y for y in shipList):
		print("hit!!!!")
		hits[nextTest] = 1
		numberOfTurns += 1
		print("turn:",  numberOfTurns)

		targetHits = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
		targetMisses = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
		targetHits[nextTest] = 1

		hit = target(targetHits, algorithm, targetMisses)
		gameBoard = hit + gameBoard
	else:
		print("miss!!")
		numberOfTurns += 1
		print("turn:",  numberOfTurns)
	gameBoard[nextTest] = 1
	print()
print("total shot placement:")
print(gameBoard)
print("final ship placement:")
print(hits)
print("total turns taken:", numberOfTurns)