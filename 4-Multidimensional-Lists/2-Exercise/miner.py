field_size = int(input())
commands = input().split()

miner_position = None
collected_coal = 0
total_coal = 0
game_over = False

field = []

for i in range(field_size):
    row = input().split()

    if "s" in row:
        miner_position = [i, row.index("s")]
    if "c" in row:
        total_coal += 1
    field.append(row)

for command in commands:
    if command == "left":
        if miner_position[1] > 0:
            miner_position[1] -= 1
    elif command == "right":
        if miner_position[1] < field_size - 1:
            miner_position[1] += 1
    elif command == "up":
        if miner_position[0] > 0:
            miner_position[0] -= 1
    elif command == "down":
        if miner_position[0] < field_size - 1:
            miner_position[0] += 1

    if field[miner_position[0]][miner_position[1]] == "e":
        print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
        game_over = True
        break
    elif field[miner_position[0]][miner_position[1]] == "c":
        collected_coal += 1
        field[miner_position[0]][miner_position[1]] = "*"

if collected_coal == total_coal:
    print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
else:
    if not game_over:
        remaining_coal = 0
        for row in field:
            remaining_coal += row.count("c")
        print(f"{remaining_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
