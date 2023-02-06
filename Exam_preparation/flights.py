def flights(*args):
    final_dict = {}
    for idx in range(0, len(args), 2):
        if args[idx] == "Finish":
            break
        else:
            final_dict[args[idx]] = final_dict.get(args[idx], 0) + args[idx + 1]

    return final_dict





print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))