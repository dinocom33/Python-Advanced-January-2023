def start_spring(**kwarg):
    spring = dict()
    for key, value in kwarg.items():
        if value not in spring:
            spring[value] = []
        spring[value].append(key)
    spring_sort = dict(sorted(spring.items(), key=lambda x: (-len(x[1]), x[0])))
    result = []
    for k, v in spring_sort.items():
        result.append(f"{k}:")
        for val in sorted(v):
            result.append(f"-{val}")
    return "\n".join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))




