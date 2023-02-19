from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

medkit = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

final_medkit = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    for kit, value in medkit.items():
        if textile + medicament == value:
            final_medkit[kit] = final_medkit.get(kit, 0)
            final_medkit[kit] += 1
            break
        elif textile + medicament > medkit["MedKit"]:
            final_medkit["MedKit"] += 1
            remaining_res = (textile + medicament) - medkit["MedKit"]
            medicaments[-1] += remaining_res
            break
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for med, value in sorted(final_medkit.items(), key=lambda x: (-x[1], x[0])):
    if value:
        print(f"{med} - {value}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
