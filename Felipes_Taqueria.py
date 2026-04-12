# 3rd Pset 2nd problem



menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }



while True:
    try:
        i = 0
        requested_item = input("Item: ").title()
        if requested_item not in menu:
            continue
        else:
            price_x = float(menu[requested_item])
            i = price_x + i

            print(f'total: ${i:.2f}')
    except EOFError:
        break
