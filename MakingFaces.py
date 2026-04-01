# /////////// Making Faces

def main():
    x = input("hey this will show you the transformation ")
    y = convert(x)
    print(y)
    

def convert(x):
    y = x.replace(":)", "😊").replace(":(", "😒")
    return y



main()
