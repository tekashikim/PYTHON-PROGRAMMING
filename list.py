# list.py
# This program demonstrates how to use lists in Python.

# Creating a list
fruits = ["Apple", "Banana", "Orange"]

print("Original list:", fruits)

# Adding an item
fruits.append("Mango")
print("After adding Mango:", fruits)

# Removing an item
fruits.remove("Banana")
print("After removing Banana:", fruits)

# Updating an item
fruits[1] = "Grapes"
print("After updating Orange to Grapes:", fruits)

# Looping through the list
print("\nItems in the list:")
for fruit in fruits:
    print(fruit)