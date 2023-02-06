size = int(input())

field = []
player_position = []
total_coins = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())

    if "P" in field[row]:
        player_position = [row, field[row].index("P")]

players_path = [player_position]

while True:
    command = input()

    if command == "up" and player_position[0] == 0:
        curr_row = player_position[0] + directions[command][0] + size
        curr_col = player_position[1] + directions[command][1]
    elif command == "down" and player_position[0] == size - 1:
        curr_row = 0
        curr_col = player_position[1] + directions[command][1]
    elif command == "left" and player_position[1] == 0:
        curr_row = player_position[0] + directions[command][0]
        curr_col = player_position[1] + directions[command][1] + size
    elif command == "right" and player_position[1] == size - 1:
        curr_row = player_position[0] + directions[command][0]
        curr_col = 0
    else:
        curr_row = player_position[0] + directions[command][0]
        curr_col = player_position[1] + directions[command][1]

    if field[curr_row][curr_col].isdigit():
        total_coins += int(field[curr_row][curr_col])

    if field[curr_row][curr_col] == "X":
        total_coins //= 2
        players_path.append([curr_row, curr_col])
        player_position = [curr_row, curr_col]
        break

    if total_coins >= 100:
        players_path.append([curr_row, curr_col])
        player_position = [curr_row, curr_col]
        break

    players_path.append([curr_row, curr_col])
    field[curr_row][curr_col] = "-"
    player_position = [curr_row, curr_col]

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")

print("Your path:")
for p in players_path:
    print(p)
