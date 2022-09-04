board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# rotate_L
import copy
N = len(board)
board_copy = copy.deepcopy(board)
for index, row in enumerate(board_copy):
    for idx, v in enumerate(row):
        board[N-idx-1][index] = v
print(board)


board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# rotate_R
import copy
N = len(board)
board_copy = copy.deepcopy(board)
for index, row in enumerate(board_copy):
    for idx, v in enumerate(row):
        board[idx][N-index-1] = v
print(board)