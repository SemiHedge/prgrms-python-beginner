board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# transpose 1
board_t1= list(zip(*board))
print(board_t1)

# transpose 2
board_t2= list(zip(*board_t1))
print(board_t2)

# rotate R2
board_r1 = list(zip(*reversed(board)))
print(board_r1)


# rotate R1
board_r1 = list(zip(*reversed(board)))
print(board_r1)

print('===== rotate_R =====')
# rotate for 4
board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(board)
for _ in range(4):
    board = list(zip(*reversed(board)))
    print(board)

# rotate L1
board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(board)
board_l1 = list(reversed(list(zip(*board))))
# board_l1 = sorted(list(zip(*board)), reverse=True)
print(board_l1)
