from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if orders[0] <= food_quantity:
        current_order = orders.popleft()
        food_quantity -= current_order
    else:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break

else:
    print("Orders complete")
