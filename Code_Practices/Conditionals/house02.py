
# Using match-case to determine the house of a person based on their name --- IGNORE ---

name = input("What is your name? ").strip().lower()

match name:
    case "ahzam":
        print("Welcome to the RED house , " + name + "!")
    case "sania":
        print("Welcome to the RED house , " + name + "!")    
    case "sami":
        print("Welcome to the BLUE house , " + name + "!")
    case "zain":
        print("Welcome to the BLUE house , " + name + "!")
    case _:
        print("Welcome to the house of your choice , " + name + "!")
         