import random 

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        
        tries = 0
        while tries < 3:
                try:
                    print(f"{x} + {y} = ", end="")
                    get_answer = int(input())
                    if get_answer == x + y:
                        score += 1
                        break
                    else:
                        tries +=1
                        print("EEE")
                        if tries == 3:
                            print(f"{x} + {y} = {x + y}")
                            break
                except ValueError:
                    continue
    print(f"Score: {score}/10")

        




def get_level():
    level_range = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in level_range:
                return level
            else:
                raise ValueError
            
        except ValueError:
            continue

def generate_integer(level):
        if level == 1:
            x = random.randint(0, 9)
            # y = random.randint(0, 9)
            return x 
        elif level == 2:
            x = random.randint(10, 99)
            return x
        else:
            x = random.randint(100, 999)
            return x

## 

# correct_answer = x + y
# get_answer = int(input())
# if get_answer == correct_answer:
#     break
# else:
#     error_count += 1
#     if error_count == 3:
#         print(correct_answer)
#         break
#     continue




# error_count = 0
# while True:
#     if level in level_range:
#         for i in range(10):
#             if level == 1:
#                 x = random.randint(0, 9)
#                 y = random.randint(0, 9)
#                 answer_format = print(f"{x} + {y} = ", end="")
#                 get_answer = int(input())


#             elif level == 2:
#                 x = random.randint(10, 99)
#                 y = random.randint(10, 99)
#             else:
#                 x = random.randint(100, 999)
#                 y = random.randint(100, 999)
            
#             calculate = int(x) + int(y) 
#             if calculate == get_answer:
#                 continue
#             else:
#                 print("EEE")
#                 error_count += 1
#                 if error_count == 3:
#                     print(get_answer, calculate)

            

#     else:
#         print("correct it") 
#         continue


main()