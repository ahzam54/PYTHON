
# Using match-case to determine the house based on the name --- IGNORE ---
# This version of the code uses the match-case statement to check for multiple names in a more

name = input("What is your name? ").strip().lower()

match name:
    case "ahzam" | "sania":
        print("Welcome to the RED house , " + name + "!")

    case "sami" | "zain":
        print("Welcome to the BLUE house , " + name + "!")

    case _:
        print("Welcome to the house of your choice , " + name + "!")