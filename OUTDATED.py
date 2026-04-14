# cs50 Lec 3 last prob

month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    try:
        middle_endian = input("DATE: ").title().replace(",", "")
        if "/" in middle_endian:
            middle_endian = middle_endian.split("/")
            if int(middle_endian[0]) <= 12 and int(middle_endian[1]) <= 31:
                
                print(f"international: {middle_endian[2].zfill(2)}-{middle_endian[0].zfill(2)}-{middle_endian[1].zfill(2)}")
                break
            else:
                continue
        

        else:
            middle_endian = middle_endian.split()
            if middle_endian[0] in month and int(middle_endian[1]) <= 31:
                get_month = month.index(middle_endian[0]) + 1
                get_month = str(get_month).zfill(2)
                print(f"{middle_endian[2].zfill(2)}-{get_month}-{middle_endian[1].zfill(2)}")
                break
            else:
                continue
    except ValueError:
        print("come on retry !!")
        continue