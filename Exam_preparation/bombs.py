from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))

bomb_types = {
    "Cherry Bombs": [60, 0],
    "Datura Bombs": [40, 0],
    "Smoke Decoy Bombs": [120, 0],
}
pouch_filled = False

while bomb_effects and bomb_casings:
    curr_effect = bomb_effects.popleft()
    curr_casings = bomb_casings.pop()
    curr_bomb = curr_effect + curr_casings

    if curr_bomb == bomb_types["Datura Bombs"][0]:
        bomb_types["Datura Bombs"][1] += 1
    elif curr_bomb == bomb_types["Cherry Bombs"][0]:
        bomb_types["Cherry Bombs"][1] += 1
    elif curr_bomb == bomb_types["Smoke Decoy Bombs"][0]:
        bomb_types["Smoke Decoy Bombs"][1] += 1
    else:
        bomb_casings.append(curr_casings - 5)
        bomb_effects.appendleft(curr_effect)

    if bomb_types["Datura Bombs"][1] >= 3 and bomb_types["Cherry Bombs"][1] >= 3 and bomb_types["Smoke Decoy Bombs"][1] >= 3:
        pouch_filled = True
        break

if pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")

for b, t in sorted(bomb_types.items()):
    print(f"{b}: {t[1]}")
