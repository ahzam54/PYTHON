name = input("What's your name? ")

file = open("names.txt" , "a") #"w" rewrite every time when we run code.. "a" append the text to next text if  we run the code again
file.write(f"{name}\n")
file.close()