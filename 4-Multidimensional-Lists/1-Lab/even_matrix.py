rows = int(input())

matrix = []

for i in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

# result = []
# for row in matrix:
#     temp_result = []
#     for el in row:
#         if el % 2 == 0:
#             temp_result.append(el)
#     result.append(temp_result)
result = [[x for x in row if x % 2 == 0] for row in matrix]

print(result)
