from math_op_module import math_operations

firs_number, operator, second_number = [x for x in input().split()]

result = math_operations(firs_number, operator, second_number)
print(f"{result: .2f}")
