
# This program assigns a house to the user based on their name.
#  It uses conditional statements to check the name and print a welcome message accordingly.
name = input("What is your name? ")

if name == "Ahzam" or name == "Sania":
    print("Welcome to the RED house , " + name + "!")
elif name == "Sami" or name == "Zain":
    print("Welcome to the BLUE house , " + name + "!")
elif name == "Ammar" or name == "Hassan":
    print("Welcome to the GREEN house , " + name + "!")
else:
    print("Welcome to the house of your choice , " + name + "!")