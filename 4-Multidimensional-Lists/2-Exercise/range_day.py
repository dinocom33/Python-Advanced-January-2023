def move(direction, steps):
    row = shooter_position[0] + (directions[direction][0] * steps)
    coll = shooter_position[1] + (directions[direction][1] * steps)

    if not (0 <= row < size and 0 <= coll < size):
        return shooter_position
    if field[row][coll] == "x":
        return shooter_position

    return [row, coll]


def shoot(direction):
    row = shooter_position[0] + directions[direction][0]
    coll = shooter_position[1] + directions[direction][1]

    while 0 <= row < size and 0 <= coll < size:
        if field[row][coll] == "x":
            field[row][coll] = "."
            return [row, coll]

        row += directions[direction][0]
        coll += directions[direction][1]

size = 5
field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

shooter_position = []
total_targets = 0
targets_down = 0
targets_down_positions = []

for row in range(size):
    field.append(input().split())

    if "A" in field[row]:
        shooter_position = [row, field[row].index("A")]
        field[row][field[row].index("A")] = "."

    if "x" in field[row]:
        total_targets += field[row].count("x")

for _ in range(int(input())):
    current_command = input().split()
    command = current_command[0]

    if command == "move":
        direction = current_command[1]
        step = int(current_command[2])
        shooter_position = move(direction, step)
    elif command == "shoot":
        shoot_direction = current_command[1]
        targets_down_pos = shoot(shoot_direction)

        if targets_down_pos:
            targets_down_positions.append(targets_down_pos)
            targets_down += 1

        if total_targets == targets_down:
            print(f"Training completed! All {targets_down} targets hit.")
            break

else:
    print(f"Training not completed! {total_targets - targets_down} targets left.")

print(*targets_down_positions, sep="\n")
