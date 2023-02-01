def shopping_cart(*products):
    menu = {"Pizza": [], "Soup": [], "Dessert": []}

    for data in products:
        if data == "Stop":
            break
        meal, product = data
        if product not in menu[meal]:
            if meal == "Pizza" and len(menu["Pizza"]) != 4:
                menu[meal].append(product)
            elif meal == "Soup" and len(menu["Soup"]) != 3:
                menu[meal].append(product)
            elif meal == "Dessert" and len(menu["Dessert"]) != 2:
                menu[meal].append(product)

    result = []
    for key, values in sorted(menu.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        for val in sorted(values):
            result.append(f" - {val}")

    if any(len(x) != 0 for x in menu.values()):
        return "\n".join(result)
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
