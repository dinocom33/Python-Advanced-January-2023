from collections import deque

present_materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while present_materials and magic_levels:
    material = present_materials.pop()
    magic = magic_levels.popleft()
    current_gift = magic + material

    if current_gift < 100:
        if current_gift % 2 == 0:
            material *= 2
            magic *= 3
            current_gift = magic + material
        elif current_gift % 2 != 0:
            current_gift *= 2
    elif current_gift > 499:
        current_gift /= 2

    if 100 <= current_gift <=199:
        presents["Gemstone"] += 1
    elif 200 <= current_gift <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= current_gift <= 399:
        presents["Gold"] += 1
    elif 400 <= current_gift <= 499:
        presents["Diamond Jewellery"] += 1

if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) or \
        (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if present_materials:
    print(f"Materials left: {', '.join(str(x) for x in present_materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, quantity in sorted(presents.items(), key=lambda x: x[0]):
    if quantity > 0:
        print(f"{present}: {quantity}")
