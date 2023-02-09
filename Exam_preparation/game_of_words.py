initial_string = list(input())
size = int(input())

matrix = []
player_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(list(input()))

    if "P" in matrix[row]:
        player_position = [row, matrix[row].index("P")]
        matrix[row][matrix[row].index("P")] = "-"

number_of_commands = int(input())

for command in range(number_of_commands):
    curr_command = input()
    curr_row = player_position[0] + directions[curr_command][0]
    curr_coll = player_position[1] + directions[curr_command][1]

    if not 0 <= curr_row < size or not 0 <= curr_coll < size:
        initial_string.pop()
        continue

    if matrix[curr_row][curr_coll] != "-":
        initial_string.append(matrix[curr_row][curr_coll])
        matrix[curr_row][curr_coll] = "-"

    player_position = [curr_row, curr_coll]

matrix[player_position[0]][player_position[1]] = "P"
print("".join(initial_string))

for row in matrix:
    print("".join(row))
