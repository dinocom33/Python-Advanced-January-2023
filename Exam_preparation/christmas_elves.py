from collections import deque

elfs_energy = deque(int(x) for x in input().split())
number_of_materials = deque(int(x) for x in input().split())

created_toys = 0
total_used_energy = 0
elfs_count = 0

while elfs_energy and number_of_materials:
    curr_elf_energy = elfs_energy.popleft()

    if curr_elf_energy < 5:
        continue
    elfs_count += 1
    material = number_of_materials.pop()

    if elfs_count % 3 == 0:
        if curr_elf_energy >= material * 2:
            if elfs_count % 5 == 0:
                elfs_energy.append(curr_elf_energy - material * 2)
            else:
                created_toys += 2
                elfs_energy.append((curr_elf_energy - (material * 2)) + 1)
            total_used_energy += material * 2
        else:
            number_of_materials.append(material)
            elfs_energy.append(curr_elf_energy * 2)
    elif elfs_count % 3 != 0:
        if curr_elf_energy >= material:
            if elfs_count % 5 == 0:
                elfs_energy.append(curr_elf_energy - material)
            else:
                created_toys += 1
                elfs_energy.append((curr_elf_energy - material) + 1)
            total_used_energy += material
        else:
            number_of_materials.append(material)
            elfs_energy.append(curr_elf_energy * 2)

print(f"Toys: {created_toys}")
print(f"Energy: {total_used_energy}")

if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")

if number_of_materials:
    print(f"Boxes left: {', '.join(str(x) for x in number_of_materials)}")
