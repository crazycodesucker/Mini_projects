#//////// Camelcase

def main():
    x = input("camelCase: ")
    convert(x)
    

def convert(x):
    for i in x:
        if i.isupper():
            print("_", end="" )
            print(i.lower(), end="")
        else:
            print(i, end="")
        
main()