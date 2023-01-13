from collections import deque

numbers = deque(input().split())
numbers.reverse()

print(" ".join(numbers))
# numbers = deque(int(x) for x in input().split())
# reversed_numbers = reversed(numbers)
#
# print(*reversed_numbers)
# while len(numbers):
#     print(numbers.pop(), end=" ")
