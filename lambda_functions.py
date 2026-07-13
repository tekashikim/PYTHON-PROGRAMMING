add = lambda a, b: a + b
print("Addition:", add(10, 20))
multiply = lambda a, b: a * b
print("Multiplication:", multiply(5, 6))
students = [("John", 75), ("Ann", 90), ("Mark", 65), ("Mary", 85)]
sorted_students = sorted(students, key=lambda student: student[1])
print("\nStudents sorted by marks:")
for student in sorted_students:
    print(student)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nEven numbers:")
print(even_numbers)
squares = list(map(lambda x: x ** 2, numbers))
print("\nSquares of the numbers:")
print(squares)