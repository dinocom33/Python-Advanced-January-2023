from collections import deque

number = int(input())

numbers_deque = deque()

for _ in range(number):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        numbers_deque.append(command[1])
    elif command[0] == 2 and numbers_deque:
        numbers_deque.pop()
    elif command[0] == 3 and numbers_deque:
        print(max(numbers_deque))
    elif command[0] == 4 and numbers_deque:
        print(min(numbers_deque))

numbers_deque.reverse()

print(*numbers_deque, sep=", ")
