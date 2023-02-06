def stock_availability(*args):
    products = list(args[0])
    info = args[1:]
    if info[-1] == "sell":
        products.pop(0)
    elif isinstance(info[-1], int):
        products = products[info[-1]:]
    else:
        for prod in info[1:]:
            if info[0] == "delivery":
                products.append(prod)
            elif prod in products:
                while prod in products:
                    products.remove(prod)

    return products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
