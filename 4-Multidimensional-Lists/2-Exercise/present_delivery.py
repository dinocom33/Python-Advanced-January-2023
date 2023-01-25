number_of_presents = int(input())
size = int(input())
neighborhood = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
santa_position = []
total_nice_kids = 0
nice_kids_with_presents = 0

for row in range(size):
    data = input().split()
    neighborhood.append(data)

    if "S" in data:
        santa_position = [row, data.index("S")]
        neighborhood[row][santa_position[1]] = "-"
    total_nice_kids += data.count("V")

command = input()

while command != "Christmas morning":
    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1]
    ]

    house = neighborhood[santa_position[0]][santa_position[1]]

    if house == "V":
        number_of_presents -= 1
        nice_kids_with_presents += 1
    elif house == "C":
        for x, y in directions.values():
            r = santa_position[0] + x
            c = santa_position[1] + y

            if neighborhood[r][c].isalpha():
                if neighborhood[r][c] == "V":
                    nice_kids_with_presents += 1

                number_of_presents -= 1
                neighborhood[r][c] = "-"

            if not number_of_presents:
                break

    neighborhood[santa_position[0]][santa_position[1]] = "-"
    if not number_of_presents or total_nice_kids == nice_kids_with_presents:
        break

    command = input()

neighborhood[santa_position[0]][santa_position[1]] = "S"

if nice_kids_with_presents < total_nice_kids and not number_of_presents:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(*row)

if total_nice_kids == nice_kids_with_presents:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_with_presents} nice kid/s.")
