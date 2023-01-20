rows = int(input())


def create_matrix(rows):
    temp_matrix = []
    for _ in range(rows):
        current_row = [int(x) for x in input().split(", ")]
        temp_matrix.append(current_row)
    return temp_matrix


matrix = create_matrix(rows)

result = [el for row in matrix for el in row]

# for row in matrix:
#     for el in row:
#         result.append(el)
# matrix = []
#
# for _ in range(rows):
#     current_row = list(map(int, input().split(", ")))
#     matrix.append(current_row)

print(result)
