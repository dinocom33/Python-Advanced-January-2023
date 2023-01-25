def sorting_cheeses(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda k: (-len(k[1]), k[0])))
    result = []
    for cheese, quantity in sorted_dict.items():
        result.append(cheese)
        quantity_sort = sorted(quantity, reverse=True)
        result.extend(quantity_sort)
    return "\n".join([str(x) for x in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
