def sum_primary_diagonal(matrix):
    sum_diagonal = 0
    primary_diagonal = []
    for i in range(len(matrix)):
        sum_diagonal += matrix[i][i]
        primary_diagonal.append(matrix[i][i])
    return sum_diagonal, primary_diagonal


def sum_secondary_diagonal(matrix):
    sum_diagonal = 0
    secondary_diagonal = []
    for i in range(len(matrix) - 1, -1, -1):
        sum_diagonal += matrix[i][(len(matrix) - 1) - i]
        secondary_diagonal.append(matrix[i][(len(matrix) - 1) - i])
    return sum_diagonal, secondary_diagonal


matrix = [[int(x) for x in input().split(", ")] for i in range(int(input()))]

sum_primary_diagonal, primary_diagonal = sum_primary_diagonal(matrix)
sum_secondary_diagonal, secondary_diagonal = sum_secondary_diagonal(matrix)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(str(x) for x in reversed(secondary_diagonal))}. Sum: {sum_secondary_diagonal}")
