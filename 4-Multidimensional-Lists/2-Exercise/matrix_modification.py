rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    row, col, value = info

    if 0 <= int(row) < len(matrix) and 0 <= int(col) < len(matrix):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*el) for el in matrix]
