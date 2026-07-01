
# This program reads names from a file called "names.txt", stores them in a list, 
# sorts the list in reverse order, and then prints a greeting for each name.
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name}")