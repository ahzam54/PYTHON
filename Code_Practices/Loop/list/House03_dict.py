
# 3: Creating a dictionary to map students to their respective house colors and printing the dictionary
'''
students = ["Ahzam", "Zain", "Ali", "Hassan", "Hussain"]
houses = ["Red", "Green", "Blue","Red", "Green"]
'''
# The above code creates two lists: one for students and one for their respective house colors.
# We can create a dictionary to map each student to their house color using the zip() function
students = {
    "Ahzam": "Red",
    "Zain": "Green",
    "Ali": "Blue",
    "Hassan": "Red",
    "Hussain": "Green"
}

# Printing the dictionary of students and their house colors
print(students["Ahzam"])  # Output: Red
print(students["Zain"])   # Output: Green
print(students["Ali"])    # Output: Blue
print(students["Hassan"]) # Output: Red
print(students["Hussain"])# Output: Green



