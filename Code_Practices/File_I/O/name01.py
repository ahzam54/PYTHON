names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)
    # pythonic way
    #names.append(input("What's your name? "))

for i in sorted(names):
    print(f"hello, {i}")