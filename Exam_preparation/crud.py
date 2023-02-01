size = 6
matrix = [[x for x in input().split()] for _ in range(size)]
firs_position = input()
position = [int(firs_position[1]), int(firs_position[-2])]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command, *info = input().split(", ")

    if command == "Stop":
        break

    curr_row = position[0] + directions[info[0]][0]
    curr_col = position[1] + directions[info[0]][1]

    if command == "Create":
        value = info[1]
        if matrix[curr_row][curr_col] == ".":
            matrix[curr_row][curr_col] = value
    elif command == "Update":
        value = info[1]
        if matrix[curr_row][curr_col].isalpha() or matrix[curr_row][curr_col].isdigit():
            matrix[curr_row][curr_col] = value
    elif command == "Delete":
        if matrix[curr_row][curr_col].isalpha() or matrix[curr_row][curr_col].isdigit():
            matrix[curr_row][curr_col] = "."
    elif command == "Read":
        if matrix[curr_row][curr_col].isalpha() or matrix[curr_row][curr_col].isdigit():
            print(matrix[curr_row][curr_col])

    position = [curr_row, curr_col]

for row in matrix:
    print(*row)
