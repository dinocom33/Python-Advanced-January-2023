size = int(input())
racing_number = input()

matrix = []
car_position = [0, 0]
finish_position = []
total_kilometers = 0
tunnels_positions = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for row in range(size):
    matrix.append(input().split())

    if "T" in matrix[row]:
        tunnels_positions.append([row, matrix[row].index("T")])

    if "F" in matrix[row]:
        finish_position = [row, matrix[row].index("F")]

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break
    curr_row = car_position[0] + directions[command][0]
    curr_col = car_position[1] + directions[command][1]

    if matrix[curr_row][curr_col] == "F":
        car_position = [curr_row, curr_col]
        total_kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
    if matrix[curr_row][curr_col] == "T":
        if [curr_row, curr_col] == tunnels_positions[0]:
            curr_row, curr_col = tunnels_positions[1]
            total_kilometers += 30
            car_position = [curr_row, curr_col]
            matrix[tunnels_positions[0][0]][tunnels_positions[0][1]] = "."
            matrix[tunnels_positions[1][0]][tunnels_positions[1][1]] = "."
            continue
        elif [curr_row, curr_col] == tunnels_positions[1]:
            curr_row, curr_col = tunnels_positions[0]
            total_kilometers += 30
            car_position = [curr_row, curr_col]
            matrix[tunnels_positions[0][0]][tunnels_positions[0][1]] = "."
            matrix[tunnels_positions[1][0]][tunnels_positions[1][1]] = "."
            continue
    total_kilometers += 10
    car_position = [curr_row, curr_col]

matrix[car_position[0]][car_position[1]] = "C"

print(f"Distance covered {total_kilometers} km.")

for row in matrix:
    print("".join(row))
