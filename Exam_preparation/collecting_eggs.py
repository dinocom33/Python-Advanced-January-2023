from collections import deque

egg_size = deque(int(x) for x in input().split(", "))
paper_size = deque(int(x) for x in input().split(", "))

box_size = 50
filled_boxes = 0

while egg_size and paper_size:
    curr_egg = egg_size.popleft()
    if curr_egg <= 0:
        continue

    if curr_egg == 13:
        first_paper = paper_size.popleft()
        last_paper = paper_size.pop()
        paper_size.appendleft(last_paper)
        paper_size.append(first_paper)
        continue

    curr_paper = paper_size.pop()
    if curr_egg + curr_paper <= box_size:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(str(x) for x in egg_size)}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")
