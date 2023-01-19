from collections import deque

numbers_of_materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

crafted_toys = dict()

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

toys_to_win = {
    1: ["Doll", "Wooden train"],
    2: ["Teddy bear", "Bicycle"],
}

while numbers_of_materials and magic_levels:
    material = numbers_of_materials.pop()
    magic = magic_levels.popleft()

    if magic == 0 and material == 0:
        continue
    elif magic == 0:
        numbers_of_materials.append(material)
        continue
    elif material == 0:
        magic_levels.appendleft(magic)
        continue

    if toys.get(material * magic):
    # if material * magic in toys:
        key = toys[material * magic]
        crafted_toys[key] = crafted_toys.get(key, 0) + 1
    elif material * magic < 0:
        numbers_of_materials.append(material + magic)
    elif material * magic > 0:
        numbers_of_materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys.keys()) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if numbers_of_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(numbers_of_materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")
