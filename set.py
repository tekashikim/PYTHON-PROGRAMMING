# set.py
# This program demonstrates how to use sets in Python.

# Creating a set (duplicate values are automatically removed)
numbers = {10, 20, 30, 40, 20, 30}

print("Original set:", numbers)

# Adding an element
numbers.add(50)
print("After adding 50:", numbers)

# Removing an element
numbers.remove(20)
print("After removing 20:", numbers)

# Showing that duplicates are removed automatically
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", duplicate_set)