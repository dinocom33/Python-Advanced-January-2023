from functools import reduce
from math import floor

initial_string = input().split()

index = 0

functions = {
    "*": lambda x: reduce(lambda a, b: int(a) * int(b), map(int, initial_string[:x])),
    "/": lambda x: reduce(lambda a, b: a / b, map(int, initial_string[:x])),
    "-": lambda x: reduce(lambda a, b: a - b, map(int, initial_string[:x])),
    "+": lambda x: reduce(lambda a, b: a + b, map(int, initial_string[:x])),
}

while index < len(initial_string):
    current_element = initial_string[index]

    if current_element in "+-*/":
        initial_string[0] = functions[current_element](index)
        [initial_string.pop(1) for i in range(index)]
        index = 0
    index += 1

print(floor(int(initial_string[0])))
