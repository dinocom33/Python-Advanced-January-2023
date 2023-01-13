from collections import deque
from datetime import datetime, timedelta

all_robots = {}

for robot in input().split(";"):
    robot_name, process_time = robot.split("-")
    all_robots[robot_name] = [int(process_time), 0]

time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    current_product = input()

    if current_product == "End":
        break

    products.append(current_product)

while products:
    time += timedelta(0, 1)
    product = products.popleft()
    free_robots = []

    for name, value in all_robots.items():
        if value[1] != 0:
            all_robots[name][1] -= 1

    for name, value in all_robots.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue
    robot_name, process_time = free_robots[0]
    all_robots[robot_name][1] = process_time[0]

    print(f"{free_robots[0][0]} - {product} [{time.strftime('%H:%M:%S')}]")
