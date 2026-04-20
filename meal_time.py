# ///////// meal time

def main():
    time = input("What is the time: ")
    if convert(time) >= 7 and convert(time)<= 8:
        print("breakfast time")
    elif convert(time) >= 12 and convert(time)<= 13:
        print("lunch time")
    elif convert(time) >= 18 and convert(time)<= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60 
    time = int(hours) + minutes
    return time

main()
