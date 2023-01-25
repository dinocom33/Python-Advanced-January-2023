def sum_diagonals(matrix):
    sum_prim_diagonal = 0
    sum_sec_diagonal = 0

    for i in range(len(matrix)):
        sum_prim_diagonal += matrix[i][i]

    for j in range(len(matrix) - 1, -1, -1):
        sum_sec_diagonal+= matrix[j][(len(matrix) - 1) - j]
    return sum_prim_diagonal, sum_sec_diagonal


n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

sum_prim_diagonal, sum_sec_diagonal = sum_diagonals(matrix)
difference = abs(sum_prim_diagonal - sum_sec_diagonal)

print(difference)
