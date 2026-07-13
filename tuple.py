# tuple.py
# This program demonstrates how to use tuples in Python.

# Creating a tuple
colors = ("Red", "Green", "Blue", "Yellow")

# Accessing tuple elements by index
print("First color:", colors[0])
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

# Displaying the entire tuple
print("All colors:", colors)

# Tuples cannot be modified.
# The code below would cause an error if uncommented.
# colors[0] = "Black"
# TypeError: 'tuple' object does not support item assignment