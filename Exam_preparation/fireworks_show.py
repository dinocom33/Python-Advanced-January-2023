from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

while firework_effects and explosive_power:
    effect = firework_effects.popleft()
    power = explosive_power.pop()

    if effect <= 0:
        explosive_power.append(power)
    elif power <= 0:
        firework_effects.appendleft(effect)
    else:
        if (effect + power) % 3 == 0 and (effect + power) % 5 != 0:
            palm_fireworks += 1
        elif (effect + power) % 5 == 0 and (effect + power) % 3 != 0:
            willow_fireworks += 1
        elif (effect + power) % 3 == 0 and (effect + power) % 5 == 0:
            crossette_fireworks += 1
        else:
            firework_effects.append(effect - 1)
            explosive_power.append(power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        break

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
