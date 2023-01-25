rows, columns = list(map(int, input(). split()))

matrix = [[x for x in input().split()] for _ in range(rows)]
squares_found = 0

for row in range(rows - 1):
    for col in range(columns - 1):

        character = matrix[row][col]
        if character == matrix[row][col + 1] and character == matrix[row + 1][col] \
                        and character == matrix[row + 1][col + 1]:
            squares_found += 1

print(squares_found)
