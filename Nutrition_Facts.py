# NUTRITION FACTS





def main():
    f = input("Fruit name : ").lower()
    print(get_calories(f))
    

def get_calories(x):
    try:
        return f"Calories: {database(x)}"
    except KeyError:
        return "Please type fruit Name!!"

def database(x):
    Fruits_Nutrition = {
                    "apple": 130,
                    "banana": 110,
                    "grapefruit": 60, 
                    "honeydew": 50, 
                    "kiwifruit": 90,
                    "lemon": 15,
                    "nectarine": 60,
                    "peach": 60,
                    "pineapple": 50,
                    "strawberries": 50,
                    "tangerine": 50                  
                    }
    return Fruits_Nutrition[x]



main()
