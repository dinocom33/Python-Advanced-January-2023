from collections import deque

orders = deque(int(x) for x in input().split(", "))
pizza_makers = deque(int(x) for x in input().split(", "))
total_pizzas_made = 0

while orders and pizza_makers:
    current_order = orders.popleft()

    if current_order <= 0:
        continue

    if current_order <= 10:
        current_employee = pizza_makers.pop()
        if current_employee == current_order:
            total_pizzas_made += current_order
        elif current_order > current_employee:
            total_pizzas_made += current_employee
            orders.appendleft(current_order - current_employee)
        elif current_employee > current_order:
            total_pizzas_made += current_order

if not orders and pizza_makers:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in pizza_makers)}")

if not pizza_makers and orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
