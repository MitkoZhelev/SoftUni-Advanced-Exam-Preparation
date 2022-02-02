map = []
size = int(input())
map = [list(input()) for _ in range(size)]


def verify_coordinates(command, i, j):
    pass


def is_valid(map, i, j):
    return 0 <= i < len(map) and 0 <= j < len(map)


def move_snake(map, i, j):
    action = input()
    while is_valid(map, i, j):
        map[i][j] = "."
        if action == "up":
            i = i - 1

        map[i][j] = "S"


positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(size):
    for j in range(size):
        if map[i][j] == "S":
            print(f"{i}{j}")
            move_snake(map, i, j)
