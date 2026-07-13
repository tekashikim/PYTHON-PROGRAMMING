# selection.py
# This program demonstrates selection statements in Python:
# if, if...else, and if...elif...else.

# Example 1: Using if statement
age = 20

if age >= 18:
    print("You are allowed to vote.")


# Example 2: Using if...else statement
score = int(input("\nEnter student's score: "))

if score >= 50:
    print("Student passed.")
else:
    print("Student failed.")


# Example 3: Using if...elif...else statement
number = int(input("\nEnter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Checking whether a number is even or odd
num = int(input("\nEnter a number to check even or odd: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Finding the largest of three numbers
print("\nFind the largest of three numbers")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)