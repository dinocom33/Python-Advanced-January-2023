from collections import deque

caffeine_milligrams = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

max_caffeine = 300
total_caffeine_drank = 0

while caffeine_milligrams and energy_drinks:
    curr_caffeine = caffeine_milligrams.pop()
    curr_drink = energy_drinks.popleft()
    caffeine_drank = curr_caffeine * curr_drink
    if caffeine_drank + total_caffeine_drank <= max_caffeine:
        total_caffeine_drank += curr_caffeine * curr_drink
    else:
        energy_drinks.append(curr_drink)
        if total_caffeine_drank - 30 > 0:
            total_caffeine_drank -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine_drank} mg caffeine.")
