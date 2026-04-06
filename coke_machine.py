# Coke Machine CS50 pset1 2nd problem 

total = 0

while total < 50:
    n = [10, 25, 5]
    a = int(input("enter amount: "))
    if a in n:
       
        total = a + total
        print("amount due ", total)
        # q = int(input())
    else:
        break
else:
    p = total - 50
    print("change owed: ", p)