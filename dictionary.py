# dictionary.py
# This program demonstrates how to use dictionaries in Python.
# Creating a dictionary representing a student
student = {
    "name": "Hirum Kiarie",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}

# Displaying the dictionary
print("Student Details:")
print(student)

# Accessing values
print("\nName:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Grade:", student["grade"])

# Updating values
student["age"] = 22
student["grade"] = "A-"
print("\nUpdated Student Details:")
print(student)