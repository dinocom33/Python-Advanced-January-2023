rows, columns = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for _ in range(rows):
    current_column = list(map(int, input().split(", ")))
    matrix.append(current_column)

for i in range(len(matrix)):
    total_sum += sum(matrix[i])

print(total_sum)
print(matrix)
