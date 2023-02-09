from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    current_female = females.popleft()
    current_male = males.pop()

    if current_female <= 0 and current_male <= 0:
        continue
    elif current_male <= 0:
        females.appendleft(current_female)
        continue
    elif current_female <= 0:
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_female == current_male:
        matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")

if males:
    result = []
    for m in reversed(males):
        result.append(str(m))
    print(f"Males left: {', '.join(result)}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
