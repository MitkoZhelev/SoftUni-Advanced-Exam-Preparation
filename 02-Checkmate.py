def search_of_king(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "K":
                find_queens(board, i, j)


def find_queens(board, i, j):
    for direction in range(len(row)):
        next_row = i + row[direction]
        next_col = j + col[direction]
        while validate_is_in_range(board, next_row, next_col):
            if board[next_row][next_col] == "Q":
                queens.append([next_row, next_col])
                break
            next_row += row[direction]
            next_col += col[direction]


def validate_is_in_range(board, i, j):
    return 0 <= i < len(board) and 0 <= j < len(board)


board = []
queens = []
for i in range(8):
    board.append([x for x in input().split(" ")])

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, 1, -1, 1, -1]

search_of_king(board)

if not queens:
    print("The king is safe!")
else:
    print(" ".join(x for x in queens))
