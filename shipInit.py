import numpy as np
boardSize = 10
gameBoard = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
hits = np.array([[0 for i in range(boardSize)] for j in range(boardSize)])
shipTypeList = [2, 3, 4, 5, 6]
shipList =      [[[0, 0], [0, 1], [0, 2], [0, 3]],
				 [[4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],
				 [[3, 3], [4, 3], [5, 3], [6, 3], [7,3]],
				 [[9, 4], [9, 5], [9, 6]],
				 [[5, 6], [5,7]]
				]