from collections import deque

chocolate = [int(x) for x in input().split(",")]
cups_of_milk = deque([int(el) for el in input().split(",")])


print(chocolate)
print(cups_of_milk)