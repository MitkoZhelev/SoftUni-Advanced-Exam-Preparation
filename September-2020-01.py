bomb_effect = [int(x) for x in input().split(", ")]
bomb_casing = [int(x) for x in input().split(", ")]
datura_bombs = 40
cherry_bombs = 60
smoke_decoy_bombs = 120

BOMBS = {
    "Cherry Bombs" : 0,
    "Datura Bombs" : 0,
    "Smoke Decoy Bombs" : 0,
}
effects_left= []
bomb_casings_left = []




def list_is_not_empty(bomb_effect,bomb_casing):
    return len(bomb_effect) > 0 and len(bomb_casing) > 0

def if_is_complete(bombs):
    is_complete = False
    for key,value in bombs.items():
        if value >= 3:
            is_complete =True
        else:
            return False
    return is_complete

while list_is_not_empty(bomb_effect,bomb_casing):
    current_casing = bomb_casing.pop()
    current_effect = bomb_effect.pop(0)

    while True:
        current_bomb = current_casing + current_effect
        if current_bomb == datura_bombs:
            BOMBS["Datura Bombs"] += 1
            break
        elif current_bomb == cherry_bombs:
            BOMBS['Cherry Bombs'] += 1
            break
        elif current_bomb == smoke_decoy_bombs:
            BOMBS['Smoke Decoy Bombs'] += 1
            break
        elif current_bomb >=40:
            current_casing = current_casing - 5
        else:
            effects_left.append(current_effect)
            bomb_casings_left.append(current_casing)
            break
    if if_is_complete(BOMBS):
        break

is_pouch_filled = False
for key,value in BOMBS.items():
    if value >= 3:
        is_pouch_filled = True
    else:
        is_pouch_filled = False

if is_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effect) == 0:
    print("Bomb Effects: empty")
else:

    print("Bomb Effects: " + ', '.join(map(str,bomb_effect)))
if len(bomb_casing) == 0:
    print("Bomb Casings: empty")
else:
    for i in bomb_casing:
        print("Bomb Casings: " + ', '.join(map(str,bomb_casing)))


for key,value in BOMBS.items():
    print(f"{key}: {value}")
















