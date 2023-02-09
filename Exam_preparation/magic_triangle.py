def get_magic_triangle(number):
    triangle = []
    for row in range(number):
        triangle.append([])
        triangle[row].append(1)
        for col in range(1, row):
            triangle[row].append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        if row != 0:
            triangle[row].append(1)
    return triangle


get_magic_triangle(5)
