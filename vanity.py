# Vanity Plates Last problem cs50p

# /////////////////// New version more professional
    
def main():
    x = input("PLATE: ")
    if check_length(x) and starts_with_two_letters(x) and alphanumeric(x) and number_check(x):
        print("Valid")
    else:
        print("invalid")
    # if check_length(x):
    #     if starts_with_two_letters(x):
    #         if alphanumeric(x): 
    #             if number_check(x):
    #                 print("passed 2")
    #             else:
    #                 print("failed")

def check_length(xin):
    if len(xin) >= 2 and len(xin) <= 6:
        return True

def starts_with_two_letters(xin):
    if xin[0:2].isalpha():
        return True
    
def alphanumeric(xin):
    if xin.isalnum():
        return True

    
def number_check(xin):
    number_found = False
    for i in xin:
        if i.isdigit():
            if i == "0" and not number_found:
                # print("invalid")
                return False
            number_found = True              
        else:
            if number_found:
                # print("invalid")
                return False
    return True


main()


