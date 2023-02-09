from module_triangle import *

while True:
    try:
        size = int(input("Please enter the size ot the triangle: "))
        print_triangle(size)
        break
    except ValueError:
        print("Wrong input! Please enter a number!\n")
