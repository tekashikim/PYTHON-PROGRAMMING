# builtin_functions.py
# This program demonstrates the use of at least 10 Python built-in functions.

# Sample data
numbers = [10, 20, 30, 40, 50]

# 1. print()
print("Numbers:", numbers)

# 2. len()
print("Length of the list:", len(numbers))

# 3. max()
print("Maximum value:", max(numbers))

# 4. min()
print("Minimum value:", min(numbers))

# 5. sum()
print("Sum of the numbers:", sum(numbers))

# 6. type()
print("Data type of numbers:", type(numbers))

# 7. sorted()
unsorted_numbers = [5, 2, 8, 1, 9]
print("Sorted list:", sorted(unsorted_numbers))

# 8. abs()
negative_number = -25
print("Absolute value:", abs(negative_number))

# 9. round()
decimal_number = 12.56789
print("Rounded value:", round(decimal_number, 2))

# 10. input()
name = input("Enter your name: ")

# Using print() again to display the user's input
print("Hello,", name + "!")