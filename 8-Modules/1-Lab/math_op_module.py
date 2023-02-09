import operator as op


def math_operations(first_num, operator, second_num):
    first_num, second_num = float(first_num), float(second_num)
    operations = {
        "/": op.truediv,
        "*": op.mul,
        "-": op.sub,
        "+": op.add,
        "^": op.pow,
    }

    return operations[operator](first_num, second_num)
