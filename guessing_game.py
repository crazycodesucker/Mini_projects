import random

# Guessing Game


while True:
    try:
        level = int(input("Level: "))
        answer = random.randint(1, level)
        print(answer)
        break
    except ValueError:
         print("int only")
         continue



while True:
    try:
        if level >= 1:
            guess = int(input("Guess: "))
            if guess >=1:
                if answer > guess:
                        print("Too Small!")
                        continue
                elif answer < guess:
                        print("Too Large!")
                        continue
                else:
                            print("Just right !!")
                            break
            else:
                 continue
            break
        else:
            continue
    
    except ValueError:
          pass