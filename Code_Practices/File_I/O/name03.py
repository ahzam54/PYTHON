name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# this code does't need closeing file.zest