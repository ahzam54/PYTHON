

students = {
    "Ahzam": "Red",
    "Zain": "Green",
    "Ali": "Blue",
    "Hassan": "Red",
    "Hussain": "Green"
}

# Printing the dictionary of students and their house colors
# using sep parameter in print function to separate the student name and house color with a comma and a space

for s in students:
    print(s, students[s], sep=", ")