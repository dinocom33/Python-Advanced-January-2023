def age_assignment(*names, **data):
    result = []
    for key, value in data.items():
        for name in names:
            if name.startswith(key):
                result.append(f"{name} is {value} years old.")

    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
