rows, columns = [int(x) for x in input().split(", ")]

workshop = []

current_row, current_coll = 0, 0
decorations_found = 0
total_gifts = 0
total_cookies = 0
total_decorations = 0
gifts_found = 0
cookies_found = 0
merry_christmas = False

for row in range(rows):
    workshop.append(input().split())

    if "Y" in workshop[row]:
        current_row, current_coll = row, workshop[row].index("Y")
        workshop[current_row][current_coll] = "x"

    if "D" in workshop[row]:
        total_decorations += workshop[row].count("D")

    if "G" in workshop[row]:
        total_gifts += workshop[row].count("G")

    if "C" in workshop[row]:
        total_cookies += workshop[row].count("C")

command = input()

while command != "End" and not merry_christmas:
    direction, steps = command.split("-")

    for step in range(int(steps)):
        if direction == "up":
            current_row -= 1
        elif direction == "down":
            current_row += 1
        elif direction == "left":
            current_coll -= 1
        elif direction == "right":
            current_coll += 1

        if current_row == rows:
            current_row = 0
        elif current_row == -1:
            current_row = rows - 1
        elif current_coll == columns:
            current_coll = 0
        elif current_coll == -1:
            current_coll = columns - 1

        current_step = workshop[current_row][current_coll]

        if current_step == "D":
            decorations_found += 1
        elif current_step == "C":
            cookies_found += 1
        elif current_step == "G":
            gifts_found += 1

        workshop[current_row][current_coll] = "x"

        if total_gifts == gifts_found and total_decorations == decorations_found and total_cookies == cookies_found:
            merry_christmas = True
            break
    if not merry_christmas:
        command = input()

workshop[current_row][current_coll] = "Y"

if merry_christmas:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {decorations_found} Christmas decorations")
print(f"- {gifts_found} Gifts")
print(f"- {cookies_found} Cookies")

for row in workshop:
    print(*row, sep=" ")
