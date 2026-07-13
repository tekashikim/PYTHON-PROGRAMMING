def add_numbers(a, b):
    return a + b
def rectangle_area(length, width):
    return length * width
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def display_student(name, admission_number, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Admission Number:", admission_number)
    print("Course:", course)
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