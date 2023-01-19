from collections import deque

working_bees = deque(int(x) for x in input().split())
all_nectar = list(int(x) for x in input().split())
symbols = deque(x for x in input().split())

functions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

honey_made = 0

while working_bees and all_nectar:
    bee = working_bees.popleft()
    nectar = all_nectar.pop()

    if bee > nectar:
        working_bees.appendleft(bee)
    elif bee < nectar:
        action = symbols.popleft()
        result = abs(functions[action](bee, nectar))
        honey_made += result

print(f"Total honey made: {honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if all_nectar:
    print(f"Nectar left: {', '.join(str(x) for x in all_nectar)}")
