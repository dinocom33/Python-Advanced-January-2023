def validate_indexes(curr_row, curr_column):
    if 0 <= curr_row < size and 0 <= curr_column < size:
        return True

    return False


def check_range(curr_row, curr_coll):
    result = 0
    for m_row, m_coll in directions.values():
        checked_row = curr_row + m_row
        checked_coll = curr_coll + m_coll
        if validate_indexes(checked_row, checked_coll) and field[checked_row][checked_coll] == "*":
            result += 1
            field[curr_row][curr_coll] = result


size = int(input())
number_of_bombs = int(input())
field = [[0 for r in range(size)] for c in range(size)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "top left": (-1, -1),
    "bottom left": (1, -1),
    "top right": (-1, 1),
    "bottom right": (1, 1),
}

for i in range(number_of_bombs):
    position = input()[1:-1].split(", ")
    row = int(position[0])
    column = int(position[1])
    field[row][column] = "*"

for r in range(size):
    for c in range(size):
        if field[r][c] != "*":
            check_range(r, c)

for r in field:
    print(" ".join(map(str, r)))
