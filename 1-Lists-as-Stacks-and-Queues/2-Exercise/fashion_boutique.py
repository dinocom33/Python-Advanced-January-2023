from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
current_rack_capacity = rack_capacity
racks_count = 1

while clothes:
    current_cloth = clothes.pop()
    if current_rack_capacity - current_cloth >= 0:
        current_rack_capacity -= current_cloth
    else:
        current_rack_capacity = rack_capacity - current_cloth
        racks_count += 1

print(racks_count)
