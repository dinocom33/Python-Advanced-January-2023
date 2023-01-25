def validate_indexes(indexes):
    if {indexes[0], indexes[2]}.issubset(range(rows)) and {indexes[1], indexes[3]}.issubset(range(columns)):
        return True
    return False


def swap(command, indexes):
    if validate_indexes(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row in matrix:
            print(*row, sep=" ")
    else:
        print("Invalid input!")

rows, columns = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap(command, info)
