def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for number in args:
            result *= number
        return result
    elif operator == "/":
        result = args[0]
        for number in args[1:]:
            result /= number
        return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
