from _collections import deque

kids_names = input().split()
number = int(input())

names_deque = deque(kids_names)
counter = 0

while len(names_deque) > 1:
    counter += 1
    if counter == number:
        kid_left = names_deque.popleft()
        print(f"Removed {kid_left}")
        counter = 0
    else:
        names_deque.append(names_deque.popleft())

print(f"Last is {names_deque.pop()}")
