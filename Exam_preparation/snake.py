def check_indexes(row, coll):
    if 0 <= row < SIZE and 0 <= coll < SIZE:
        return True
    return False


SIZE = int(input())

field = []
snake_pos = []
burrow_pos = []
food_eaten = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for r in range(SIZE):
    curr_row = list(input())
    field.append(curr_row)

    if "S" in curr_row:
        snake_pos = [r, curr_row.index("S")]
        field[snake_pos[0]][snake_pos[1]] = "."

    if "B" in curr_row:
        burrow_pos.append([r, curr_row.index("B")])

while True:
    command = input()
    row = snake_pos[0] + directions[command][0]
    column = snake_pos[1] + directions[command][1]

    if not check_indexes(row, column):
        print("Game over!")
        break
    else:
        if field[row][column] == "*":
            food_eaten += 1
        elif field[row][column] == "B":
            field[row][column] = "."
            if row == burrow_pos[0][0] and column == burrow_pos[0][1]:
                row = burrow_pos[1][0]
                column = burrow_pos[1][1]
            elif row == burrow_pos[1][0] and column == burrow_pos[1][1]:
                row = burrow_pos[0][0]
                column = burrow_pos[0][1]

    snake_pos = [row, column]
    field[row][column] = "."

    if food_eaten >= 10:
        print("You won! You fed the snake.")
        break

if food_eaten >= 10:
    field[snake_pos[0]][snake_pos[1]] = "S"

print(f"Food eaten: {food_eaten}")

[print("".join(row)) for row in field]
