field_size = int(input())
field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

submarine_pos = []
cruisers = 0
mines = 0
submarine_hit = 0
for row in range(field_size):
    curr_field = list(input())
    field.append(curr_field)

    if "S" in field[row]:
        submarine_pos = [row, field[row].index("S")]
        field[submarine_pos[0]][submarine_pos[1]] = "-"

    if "C" in field[row]:
        cruisers += field[row].count("C")

    if "*" in field[row]:
        mines += field[row].count("*")

while cruisers and submarine_hit != 3:
    command = input()
    curr_row = submarine_pos[0] + directions[command][0]
    curr_col = submarine_pos[1] + directions[command][1]

    if field[curr_row][curr_col] == "*":
        submarine_hit += 1
    elif field[curr_row][curr_col] == "C":
        cruisers -= 1
    submarine_pos = [curr_row, curr_col]
    field[curr_row][curr_col] = "-"

field[submarine_pos[0]][submarine_pos[1]] = "S"

if cruisers == 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

if submarine_hit == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")

for row in field:
    print("".join(row))
