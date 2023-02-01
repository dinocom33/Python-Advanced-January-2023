from collections import deque

bowls = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    curr_bowl = bowls.pop()
    curr_customer = customers.popleft()

    if curr_bowl == curr_customer:
        continue

    if curr_bowl > curr_customer:
        bowls.append(curr_bowl - curr_customer)
    elif curr_customer > curr_bowl:
        customers.appendleft(curr_customer - curr_bowl)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
