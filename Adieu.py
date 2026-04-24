import inflect
inflect_operations = inflect.engine()

# version 1 passes cs50 self-check but not cooler

# names = []
# while True:
#     try:
#         names_input = input("Enter names: ")
#         names.append(names_input)
#     except EOFError:
#         # for name in names:
#         names = inflect_operations.join(names)
#         # print("201", names)
#         print(f"Adieu, adieu, to {names}")
#         break

# version 2 but more cooler 

names = []
while True:
    try:
        names_input = input("Enter names: ")
        names.append(names_input)
        # print(names)
    except EOFError:
            for i in range(len(names)):
                pyramid_print = inflect_operations.join(names[:i+1])
                print(f"Adieu, adieu, to {pyramid_print}")
            break


#print with first name
# print along with second name








































# # name = input("Enter names: ").split()
# x = inflect_operations.join(input("Enter names: ").split())
# print(x)