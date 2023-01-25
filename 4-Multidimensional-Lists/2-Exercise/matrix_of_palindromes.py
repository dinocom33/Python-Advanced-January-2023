rows, columns = list(map(int, input().split()))

start = ord('a')

matrix = [[chr(start + i) + chr(start + j + i) + chr(start + i) for j in range(columns)] for i in range(rows)]

for row in matrix:
    print(" ".join(row))
