#// math interpreter 

e = input("expression: ").split(" ")
x = int(e[0])
y = e[1]
z = int(e[2])

match y:
    case "+":
        t = x + z
        print(f"{t:.1f}")
    case "-":
        t = x - z
        print(f"{t:.1f}")
    case "*":
        t = x * z
        print(f"{t:.1f}")
    case "/":
        t = x / z
        print(f"{t:.1f}")
