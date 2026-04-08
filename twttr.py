
## ////////  twitter CS50 pset1 3rd problem 




x = input("Input string: ").strip()
print(x)
for i in x:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print("", end="")
    else:
        print(i, end="")

print("a" in "aeiouAEIOU")  # True
print("b" in "aeiouAEIOU")  # False