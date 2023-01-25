size = int(input())
matrix = []
alice_position = []
collected_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[row][matrix[row].index("A")] = "*"

while collected_tea < 10:
    command = input()
    curr_row, curr_col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if not (0 <= curr_row < size and 0 <= curr_col < size):
        break

    alice_position = [curr_row, curr_col]
    curr_position = matrix[curr_row][curr_col]
    matrix[curr_row][curr_col] = "*"

    if curr_position == "R":
        break

    if curr_position.isdigit():
        collected_tea += int(curr_position)

if collected_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)
