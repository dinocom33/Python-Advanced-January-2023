from collections import deque

size = 6

matrix = []
rover_position = []
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if "E" in matrix[row]:
        rover_position = [row, matrix[row].index("E")]

commands = deque(input().split(", "))

while commands:
    curr_command = commands.popleft()
    curr_row = 0
    curr_col = 0
    if curr_command == "up" and rover_position[0] == 0:
        curr_row = rover_position[0] + directions[curr_command][0] + 6
        curr_col = rover_position[1] + directions[curr_command][1]
    elif curr_command == "down" and rover_position[0] == size - 1:
        curr_row = 0
        curr_col = rover_position[1] + directions[curr_command][1]
    elif curr_command == "left" and rover_position[1] == 0:
        curr_row = rover_position[0] + directions[curr_command][0]
        curr_col = rover_position[1] + directions[curr_command][1] + 6
    elif curr_command == "right" and rover_position[1] == size - 1:
        curr_row = rover_position[0] + directions[curr_command][0]
        curr_col = 0
    else:
        curr_row = rover_position[0] + directions[curr_command][0]
        curr_col = rover_position[1] + directions[curr_command][1]

    if matrix[curr_row][curr_col] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({curr_row}, {curr_col})")
    elif matrix[curr_row][curr_col] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({curr_row}, {curr_col})")
    elif matrix[curr_row][curr_col] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({curr_row}, {curr_col})")
    elif matrix[curr_row][curr_col] == "R":
        print(f"Rover got broken at ({curr_row}, {curr_col})")
        break

    rover_position = [curr_row, curr_col]

if metal_deposit > 0 and concrete_deposit > 0 and water_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
