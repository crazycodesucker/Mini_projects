# fuel guage frinal version


while True:
    try:
        a, b = input("Fraction: ").split("/") 
        if a > b:
            continue
        a = int(a) #3
        b = int(b) #4
        x = round(a / b * 100)
        x = int(x)
        if x <= 1:
           print("E")
           break
        elif x >= 99:
            print("F")
            break
        else:
            print(x, "%", sep="")
            break
        

    except ZeroDivisionError:
        print("Can't devide by zero")
    except ValueError:
        print("try this format x/y")
