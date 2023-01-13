from collections import deque

numbers = deque()

operations_functions = {
    1: lambda x: numbers.append(x),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    command = [int(x) for x in input().split()]
    if len(command) > 1:
        action, value = command[0], command[1]
        operations_functions[action](value)
    else:
        action = command[0]

        operations_functions[action](None)

numbers.reverse()

print(*numbers, sep=", ")
