cycles = [int(x) for x in input().split(", ")]

element_to_prioritize = int(input())

numbered_jobs = sorted([(v, i) for i, v in enumerate(cycles)])
count = 0
for element, index in numbered_jobs:
    count += element

    if index == element_to_prioritize:
        break

print(count)
