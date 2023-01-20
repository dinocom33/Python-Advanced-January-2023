def create_matrix(rows):
    temp_matrix = []
    for _ in range(rows):
        current_row = list(map(int, input().split(", ")))
        temp_matrix.append(current_row)
    return temp_matrix

rows, columns = list(map(int, input().split(", ")))
matrix = create_matrix(rows)


def find_sum(matrix):
    biggest_sum = 0
    submatrix = None
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            curr_submatrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
            curr_sum = sum(map(sum, curr_submatrix))
            if curr_sum > biggest_sum:
                biggest_sum = curr_sum
                submatrix = curr_submatrix

    return biggest_sum, submatrix


sum, submatrix = find_sum(matrix)

for row in submatrix:
    print(*row, sep=" ")

print(sum)
