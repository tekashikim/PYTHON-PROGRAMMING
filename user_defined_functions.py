# user_defined_functions.py
# This program demonstrates user-defined functions in Python.

# Function to add two numbers
def add_numbers(a, b):
    return a + b


# Function to find the area of a rectangle
def rectangle_area(length, width):
    return length * width


# Function to check whether a number is prime
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Function to find the factorial of a number
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# Function to display a student's details
def display_student(name, admission_number, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Admission Number:", admission_number)
    print("Course:", course)


# Calling the functions
print("Addition:", add_numbers(15, 25))

print("Area of Rectangle:", rectangle_area(8, 5))

number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))

display_student("Hirum Kiarie", "CS12345", "Computer Science")