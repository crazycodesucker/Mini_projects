##version 1

# import sys
# import pyfiglet

# name = input("Input: ")
# if len(sys.argv) == 3:
#     if sys.argv[1] == "-f" or "--font":
#         print(pyfiglet.figlet_format(name, font=sys.argv[2]))
    
#     sys.exit()
# elif len(sys.argv) == 1:
#         print(pyfiglet.figlet_format(name))
# else:
#      print("invalid usage")
#      sys.exit()

# version 2 

# import sys
# import pyfiglet


# if len(sys.argv) == 3:
#     if sys.argv[1] == "-f" or "--font":
#         name = input("Input: ")
#         print(pyfiglet.figlet_format(name, font=sys.argv[2]))
    
#     sys.exit()
# elif len(sys.argv) == 1:
#         name = input("Input: ")
#         print(pyfiglet.figlet_format(name))
# else:
#      print("invalid usage")
#      sys.exit()

# version 3 with random text

import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

random_gen = random.choice(figlet.getFonts())

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        name = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(name))
    
    sys.exit()
elif len(sys.argv) == 1:
        name = input("Input: ")
        figlet.setFont(font=random_gen)
        print(figlet.renderText(name))
else:
     print("invalid usage")
     sys.exit()

