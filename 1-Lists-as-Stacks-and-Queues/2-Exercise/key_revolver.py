from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
number_of_bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence_value = int(input())

current_gun_barrel = gun_barrel

while locks and number_of_bullets:
    current_bullet = number_of_bullets.pop()
    current_lock = locks.popleft()
    if current_lock >= current_bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    current_gun_barrel -= 1
    intelligence_value -= bullet_price
    if current_gun_barrel == 0 and len(number_of_bullets) > 0:
        print("Reloading!")
        current_gun_barrel = gun_barrel

if not locks:
    print(f"{len(number_of_bullets)} bullets left. Earned ${intelligence_value}" )
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
