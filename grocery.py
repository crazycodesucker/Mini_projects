# ////////      Grocery list

i = 0
grocery_list = {}

while True: 
    try:
        item = input("Item: ").strip().lower()
        if item in grocery_list:
                      grocery_list[item] += 1
        else:
                      if item not in grocery_list:
                            grocery_list[item] = 1
                                   
    except EOFError:
                for key, value in sorted(grocery_list.items()):
                        print(f'{value} {key.upper()}')
                
                break

