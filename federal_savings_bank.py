#1st pset 2nd problem

def main():
    get_greetings = input("Greetings: ").strip().lower()
    print(value(f"${get_greetings}"))



def value(x):
    x = x.lower()
    if x == "hello":
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


