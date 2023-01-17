numbers = int(input())

longest_intersection = set()

for _ in range(numbers):
    first_data, second_data = [element.split(",") for element in input().split("-")]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    current_intersection = set(first_range.intersection(second_range))
    if len(longest_intersection) < len(current_intersection):
        longest_intersection = current_intersection


print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length "
      f"{len(longest_intersection)}")
