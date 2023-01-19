from collections import deque

initial_string = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

colors_found = []

while initial_string:
    first_part = initial_string.popleft()
    second_part = initial_string.pop() if initial_string else ""

    if first_part + second_part in all_colors:
        colors_found.append(first_part + second_part)
    elif second_part + first_part in all_colors:
        colors_found.append(second_part + first_part)
    else:
        middle = len(initial_string) // 2
        if first_part[:-1]:
            initial_string.insert(middle, first_part[:-1])

        if second_part[:-1]:
            initial_string.insert(middle, second_part[:-1])

for color in set(secondary_colors.keys()).intersection(colors_found):
    if not secondary_colors[color].issubset(colors_found):
        colors_found.remove(color)

print(colors_found)
