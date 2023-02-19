def shop_from_grocery_list(budget, grocery_list, *products):
    money_left = budget
    final_list = {}

    for product, price in products:
        if product in grocery_list:
            if money_left >= price:
                money_left -= price
                grocery_list.remove(product)
                final_list[product] = price
            else:
                break

    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        return f"Shopping is successful. Remaining budget: {money_left:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))



