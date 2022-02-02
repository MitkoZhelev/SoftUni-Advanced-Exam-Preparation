from collections import deque
milkshakes = 0
chocolate = [int(x) for x in input().split(",")]
cups_of_milk = deque([int(el) for el in input().split(",")])


def is_completed(chocolate, cups_of_milk, milshakes):
    return (len(chocolate) > 0 and len(cups_of_milk) > 0) and milshakes < 5


while is_completed(chocolate, cups_of_milk, milkshakes):

    if len(chocolate) > 0 and chocolate[len(chocolate) - 1] <= 0:
        chocolate.remove(chocolate[-1])
    if len(cups_of_milk) > 0 and cups_of_milk[0] <= 0:
        del cups_of_milk[0]
    if not is_completed(chocolate,cups_of_milk,milkshakes):
        break

    if chocolate[len(chocolate) - 1] == cups_of_milk[0]:
        milkshakes += 1
        chocolate.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolate[len(chocolate) - 1] -= 5




if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) == 0:
    print("Chocolate: empty")
else:

    print("Chocolate: " + ', '.join(map(str, chocolate)))

if len(cups_of_milk) == 0:
    print("Milk: empty")
else:

    print(f"Milk: {', '.join(map(str,cups_of_milk))}")
