from math import log

number = int(input("Please enter a number: "))
base = input("Please enter a base: ")

if base == "natural":
    print(f"Natural logarithm is: {log(number):.2f}")
else:
    print(f"Logarithm from {number} with base {base} is: {log(number, int(base))}")
