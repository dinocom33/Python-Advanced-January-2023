from collections import deque


def list_manipulator(*data):
    given_list = deque(data[0])
    operation = data[1]
    param = data[2]

    if operation == "remove":
        if param == "end":
            if len(data) > 3:
                for i in range(data[3]):
                    given_list.pop()
            else:
                given_list.pop()

        elif param == "beginning":
            if len(data) > 3:
                for i in range(data[3]):
                    given_list.popleft()
            else:
                given_list.popleft()

    elif operation == "add":
        if param == "end":
            for i in range(3, len(data)):
                given_list.append(data[i])

        elif param == "beginning":
            for i in range(len(data) - 1, 2, -1):
                given_list.appendleft(data[i])
    result = list(given_list)
    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
