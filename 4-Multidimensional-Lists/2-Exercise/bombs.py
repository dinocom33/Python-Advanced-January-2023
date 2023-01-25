def detonate_bombs(matrix, bomb_coords):
    for coord in bomb_coords:
        row, col = coord
        damage = matrix[row][col]
        if damage <= 0:
            continue
        matrix[row][col] = 0
        for i in range(max(0, row-1), min(len(matrix), row+2)):
            for j in range(max(0, col-1), min(len(matrix[i]), col+2)):
                if matrix[i][j] > 0:
                    matrix[i][j] = matrix[i][j] - damage
    return matrix

def count_alive_cells(matrix):
    count = 0
    total = 0
    for row in matrix:
        for cell in row:
            if cell > 0:
                count += 1
                total += cell
    return count, total

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

bomb_coords = [[int(x) for x in coord.split(',')] for coord in input().split()]

matrix = detonate_bombs(matrix, bomb_coords)
alive_cells, sum_of_cells = count_alive_cells(matrix)
print("Alive cells:", alive_cells)
print("Sum:", sum_of_cells)
for row in matrix:
    print(" ".join(str(x) for x in row))
