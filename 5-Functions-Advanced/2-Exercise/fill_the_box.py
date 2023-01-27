def fill_the_box(*data):
    height = data[0]
    length = data[1]
    width = data[2]
    box_size = height * width * length
    sum_of_cubes = 0
    for num in data[3:]:
        if num == "Finish":
            break
        sum_of_cubes += num
    if box_size >= sum_of_cubes:
        return f"There is free space in the box. You could put {box_size - sum_of_cubes} more cubes."
    else:
        return f"No more free space! You have {sum_of_cubes - box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))