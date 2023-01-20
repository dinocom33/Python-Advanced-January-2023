def create_matrix():
    rows = int(input())
    temp_matrix = []
    for _ in range(rows):
        current_row = list(input())
        temp_matrix.append(current_row)
    return temp_matrix

matrix = create_matrix()

special_symbol = input()


def find_symbol(matrix, symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_symbol = matrix[i][j]
            if current_symbol == symbol:
                return i, j

result = find_symbol(matrix, special_symbol)

if result:
    print(result)
else:
    print(f"{special_symbol} does not occur in the matrix")
