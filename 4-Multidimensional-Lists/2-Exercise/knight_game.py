def check_indexes(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())
board = [list(input()) for _ in range(size)]

directions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_position = []

    for row in range(size):
        for col in range(size):
            if board[row][col] == "K":
                curr_attacks = 0

                for position in directions:
                    current_row = row + position[0]
                    current_col = col + position[1]
                    if check_indexes(current_row, current_col):
                        if board[current_row][current_col] == "K":
                            curr_attacks += 1
                if curr_attacks > max_attacks:
                    knight_position = [row, col]
                    max_attacks = curr_attacks
    if knight_position:
        board[knight_position[0]][knight_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
