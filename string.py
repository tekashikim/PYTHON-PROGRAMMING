# string.py
# This program demonstrates string operations in Python.

# Creating strings
first_name = "Hirum"
last_name = "Kiarie"

# String concatenation
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String indexing
print("First character:", full_name[0])
print("Last character:", full_name[-1])

# String slicing
print("First Name:", full_name[:5])
print("Last Name:", full_name[6:])

# String methods
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Replace:", full_name.replace("Hirum", "Tekashi"))
print("Split:", full_name.split())