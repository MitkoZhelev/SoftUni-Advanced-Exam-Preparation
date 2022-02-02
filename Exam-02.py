



shotgun_range = []
targets_hit = []
for i in range(5):
    shotgun_range.append([x for x in input().split(" ")])

commands = int(input())

def find_shooter (shotgun_range):

    for i in range(len(shotgun_range)):
        for j in range(len(shotgun_range)):
            if shotgun_range[i][j] == 'A':
                return i,j


def targets_counter (shotgun_range):
    counter = 0
    for i in range(5):
        for j in range(5):
            if shotgun_range[i][j] == "x":
                counter +=1
    return counter


def is_valid_move(shotgun_range,row,col):
    return 0 <= row < len(shotgun_range) and 0 <= col < len(shotgun_range)



def shoot(shotgun_range,direction,row,col):

    if direction == "up":
        new_row = row
        while is_valid_move(shotgun_range,new_row,col):
            if shotgun_range[new_row][col] == "x":
                targets_hit.append([new_row,col])
                shotgun_range[new_row][col] = "."
                break
            new_col = new_col + 1
    if direction == "down":
        new_row = row
        while is_valid_move(shotgun_range,new_row,col):
            if shotgun_range[new_row][col] == "x":
                targets_hit.append([new_row, col])
                shotgun_range[new_row][col] = "."
                break
            new_row = new_row + 1
    if direction == "left":
        new_col = col
        while is_valid_move(shotgun_range,row,new_col):
            if shotgun_range[row][new_col] == "x":
                targets_hit.append([row, new_col])
                shotgun_range[row][new_col] = "."
                break
            new_col = new_col - 1

    if direction == "right":
        new_col = col
        while is_valid_move(shotgun_range,row,new_col):
            if shotgun_range[row][new_col] == "x":
                targets_hit.append([row, new_col])
                shotgun_range[row][new_col] = "."
                break
            new_col = new_col + 1

    return shotgun_range

def move(shotgun_range,direction,how_many_tiles,row,col):
    if direction == "up":
        new_row = row - how_many_tiles
        if is_valid_move(shotgun_range,new_row,col):
            if shotgun_range[new_row][col] == ".":
                shotgun_range[row][col] = "."
                shotgun_range[new_row][col] = 'A'
    if direction == "down":
        new_row = row + how_many_tiles
        if is_valid_move(shotgun_range,new_row,col):
            if shotgun_range[new_row][col] == ".":
                shotgun_range[row][col] = "."
                shotgun_range[new_row][col] = 'A'
    if direction == "left":
        new_col = col - how_many_tiles
        if is_valid_move(shotgun_range,row,new_col):
            if shotgun_range[row][new_col] == ".":
                shotgun_range[row][col] = "."
                shotgun_range[row][new_col] = 'A'
    if direction == "right":
        new_col = col + how_many_tiles
        if is_valid_move(shotgun_range,row,new_col):
            if shotgun_range[row][new_col] == ".":
                shotgun_range[row][col] = "."
                shotgun_range[row][new_col] = 'A'

    return find_shooter(shotgun_range)





row,col = find_shooter(shotgun_range)


for i in range(commands):
    command = input().split(" ")
    if command[0]== "move":
     row,col =   move(shotgun_range,command[1],int(command[2]),row,col)
    elif command [0] == "shoot":
        shotgun_range = shoot(shotgun_range,command[1],row,col)

target_count = targets_counter(shotgun_range)


if (target_count == 0):
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {target_count} targets left.")

for el in targets_hit:
    print(el)
