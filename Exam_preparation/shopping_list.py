def shopping_list(budget, **kwargs):
    min_budget = 100
    max_products_in_bucket = 5
    all_products = {}
    final_bucket = []
    if budget < min_budget:
        return "You do not have enough budget."

    if kwargs:
        for product, data in kwargs.items():
            quantity, price = data
            total_price = quantity * price

            if len(all_products) == max_products_in_bucket:
                break
            else:
                if product not in all_products:
                    if total_price <= budget:
                        all_products[product] = all_products.get(product, 0)
                        all_products[product] = total_price
                        budget -= total_price
                        final_bucket.append(f"You bought {product} for {total_price:.2f} leva.")

    return "\n".join(final_bucket)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

