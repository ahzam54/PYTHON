
# Using conditionals to determine if a person can enter a house 
# based on their name. Each name corresponds to a specific house color.
#  The program prompts the user for their name and then uses a series of 
# if-elif statements to check the name against predefined names and print
# a welcome message with the corresponding house color. If the name does 
# not match any of the predefined names, no message will be printed.
name = input("What is your name? ")

if name == "Ahzam":
    print("Welcome to the RED house , Ahzam!")
elif name == "Sami":
    print("Welcome to the BLUE house , Sami!")
elif name == "Ammar":
    print("Welcome to the GREEN house , Ammar!")
elif name == "Hassan":
    print("Welcome to the YELLOW house , Hassan!")
elif name == "Zain":
    print("Welcome to the Blue house , Zain!")
elif name == "Sania":
    print("Welcome to the Red house , Sania!")
else:
    print("Welcome to the house of your choice , " + name + "!")