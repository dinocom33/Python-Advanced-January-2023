numbers = [int(x) for x in input().split()]
target_number = int(input())

targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target_number}")
    else:
        result_number = target_number - value
        targets.add(result_number)
        values_map[result_number] = value
