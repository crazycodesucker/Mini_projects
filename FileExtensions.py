x = input("hey enter your filename with extension: ").lower().split(".")


#/// method 1 
if x.endswith(".jpg"):
    y = x.strip(".jpg")
    print("image/jpg")
else:
    print("no")

#////// method 2 but lengthier
if x[1] == "jpeg":
    print("image/jpeg")
elif x[1] == "gif":
    print("image/gif")
elif x[1] == "jpg":
    print("image/jpg")
elif x[1] == "png":
    print("image/png")
elif x[1] == "pdf":
    print("application/pdf")
elif x[1] == "txt":
    print("text/plain")
elif x[1] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")


#/// method 3 

match x[1]:
    case "jpeg":
        print("image/jpeg")
    case "jpg":
        print("images/jpg")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
