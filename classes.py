# classes.py
# This program demonstrates the use of classes and objects in Python.

# Creating a class named Student
class Student:
    # Constructor to initialize object attributes
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    # Method to display student information
    def display_info(self):
        print("Student Details")
        print("Name:", self.name)
        print("Admission Number:", self.admission_number)
        print("Course:", self.course)
        print("-" * 30)


# Creating three Student objects
student1 = Student("Hirum Kiarie", "CS001", "Computer Science")
student2 = Student("John Mwangi", "CS002", "Information Technology")
student3 = Student("Mary Wanjiku", "CS003", "Software Engineering")

# Displaying their information
student1.display_info()
student2.display_info()
student3.display_info()