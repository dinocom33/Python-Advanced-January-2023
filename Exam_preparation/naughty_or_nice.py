def naughty_or_nice_list(*args, **kwargs):
    name_list = args[0]
    commands = args[1:]
    final_dict = {"Nice": [], "Naughty": [], "Not found": []}
    for command in commands:
        number, behavior = command.split("-")
        if sum(1 for num, name in name_list if int(number) == num) == 1:
            for index, child in enumerate(name_list):
                child_num, child_name = int(child[0]), child[1]
                if child_num == int(number):
                    final_dict[behavior].append(child_name)
                    del name_list[index]

    for key, value in kwargs.items():
        if sum(1 for num, name in name_list if key == name) == 1:
            for index, (num, name) in enumerate(name_list):
                if key == name:
                    final_dict[value].append(name)
                    del name_list[index]

    for index, (num, name) in enumerate(name_list):
        final_dict["Not found"].append(name)

    result = []

    for key, value in final_dict.items():
        if value:
            result.append(f"{key}: {', '.join(value)}")

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))


