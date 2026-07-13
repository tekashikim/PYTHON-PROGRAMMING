# lambda_functions.py
# This program demonstrates the use of lambda functions in Python.

# 1. Lambda function to add two numbers
add = lambda a, b: a + b
print("Addition:", add(10, 20))


# 2. Lambda function to multiply two numbers
multiply = lambda a, b: a * b
print("Multiplication:", multiply(5, 6))


# 3. Using lambda to sort a list of tuples by the second value
students = [("John", 75), ("Alice", 90), ("Brian", 65), ("Mary", 85)]

sorted_students = sorted(students, key=lambda student: student[1])

print("\nStudents sorted by marks:")
for student in sorted_students:
    print(student)


# 4. Using filter() with a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nEven numbers:")
print(even_numbers)


# 5. Using map() with a lambda function
squares = list(map(lambda x: x ** 2, numbers))

print("\nSquares of the numbers:")
print(squares)