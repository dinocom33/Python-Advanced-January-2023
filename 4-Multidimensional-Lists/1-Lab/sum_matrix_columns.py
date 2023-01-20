rows, columns = map(int, input().split(", "))

matrix = []

for _ in range(rows):
    current_row = list(map(int, input().split()))
    # current_row = [int(x) for x in input().split(" ")]
    matrix.append(current_row)

total_sum = []

for column_index in range(columns):
    result = 0
    for row_index in range(rows):
        result += matrix[row_index][column_index]
    total_sum.append(result)
#     print(result)

print(*total_sum, sep="\n")
