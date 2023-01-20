def create_matrix(rows):
    temp_matrix = []
    for _ in range(rows):
        current_row = [int(x) for x in input().split(" ")]
        temp_matrix.append(current_row)
    return temp_matrix

rows = int(input())

matrix = create_matrix(rows)

# sum_diagonal = sum(matrix[rows - i - 1][rows - i - 1] for i in range(rows))

sum_diagonal = 0

for i in range(rows):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
