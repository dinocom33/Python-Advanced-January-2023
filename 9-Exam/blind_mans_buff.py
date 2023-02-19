def valid_indexes(row, coll):
    if 0 <= row < N and 0 <= coll < M:
        return True
    return False


N, M = map(int, input().split())

playground = []
player_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

touched_opponents = 0
moves_made = 0

for row in range(N):
    playground.append(input().split())

    if "B" in playground[row]:
        player_pos = [row, playground[row].index("B")]
        playground[row][playground[row].index("B")] = "-"

while True:
    command = input()

    if command == "Finish":
        break

    curr_row = player_pos[0] + directions[command][0]
    curr_col = player_pos[1] + directions[command][1]

    if not valid_indexes(curr_row, curr_col):
        continue

    if playground[curr_row][curr_col] == "O":
        continue
    elif playground[curr_row][curr_col] == "P":
        touched_opponents += 1
        moves_made += 1
        playground[curr_row][curr_col] = "-"
    elif playground[curr_row][curr_col] == "-":
        moves_made += 1

    player_pos = [curr_row, curr_col]

    if touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
