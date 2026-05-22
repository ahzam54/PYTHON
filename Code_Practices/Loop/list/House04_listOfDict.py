
students = [
    {"name": "Ahzam", "house": "Red", "age": 20},
    {"name": "Zain", "house": "Green", "age": 21},
    {"name": "Ali", "house": "Blue", "age": 22},
    {"name": "Hassan", "house": "Red", "age": 23},
    {"name": "Hussain", "house": "Green", "age": None}
]

# Printing the list of dictionaries of students and their house colors and ages
# using sep parameter in print function to separate the student name, house color and age with a comma and a space
for s in students:
    print(s["name"], s["house"],s["age"], sep=", ")