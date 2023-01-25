size = int(input())
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bunny_position = []
max_collected_eggs = 0
best_path = []
best_direction = None

for row in range(size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

for direction, coordinates in directions.items():
    curr_row, curr_col = [
        bunny_position[0] + coordinates[0],
        bunny_position[1] + coordinates[1],
    ]
    curr_collected_egs = 0
    curr_path = []

    while 0 <= curr_row < size and 0 <= curr_col < size:
        if matrix[curr_row][curr_col] == "X":
            break

        curr_collected_egs += int(matrix[curr_row][curr_col])
        curr_path.append([curr_row, curr_col])

        curr_row += coordinates[0]
        curr_col += coordinates[1]

    if curr_collected_egs >= max_collected_eggs:
        max_collected_eggs = curr_collected_egs
        best_direction = direction
        best_path = curr_path

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)
