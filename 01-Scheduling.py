def print_board(fixed_board):
    print(fixed_board)


def validity_of_coordinates(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board)


def find_position_of_knights(board, size):
    temp_counter = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
               temp_counter = most_volatile_knight(board,i, j)


def most_volatile_knight(board,row, col):
    potential_rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    potential_cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    counter = 0
    for i in range(len(potential_rows)):
        if validity_of_coordinates(board,potential_rows[i]+row,potential_cols[i] + col):
            if board[potential_rows[i] + row][potential_cols[i]+col] == "K":
                counter +=1
    return counter




board = [list(input()) for _ in range(int(input()))]
find_position_of_knights(board, len(board))
