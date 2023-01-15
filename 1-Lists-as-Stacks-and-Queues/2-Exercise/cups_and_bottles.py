from collections import deque

cups_capacity = [int(x) for x in input().split()]
bottle_capacity = deque(int(x) for x in input().split())

wasted_water = 0

while cups_capacity and bottle_capacity:
    current_bottle = bottle_capacity.pop()
    cups_capacity[0] -= current_bottle
    if cups_capacity[0] <= 0:
        wasted_water += abs(cups_capacity.pop(0))

if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
elif bottle_capacity:
    print(f"Bottles: {' '.join(str(x) for x in bottle_capacity)}")

print(f"Wasted litters of water: {wasted_water}")
