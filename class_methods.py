# class_methods.py
# This program demonstrates the use of a constructor,
# instance variables, a class variable, and a class method.

class Student:
    # Class variable
    school_name = "The Cooperative University of Kenya"

    # Constructor
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    # Instance method
    def display_info(self):
        print("Student Details")
        print("Name:", self.name)
        print("Admission Number:", self.admission_number)
        print("Course:", self.course)
        print("School:", Student.school_name)
        print("-" * 35)

    # Class method
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


# Creating Student objects
student1 = Student("Hirum Kiarie", "CS001", "Computer Science")
student2 = Student("John Mwangi", "CS002", "Information Technology")
student3 = Student("Mary Wanjiku", "CS003", "Software Engineering")

print("Before changing the school name:\n")
student1.display_info()
student2.display_info()
student3.display_info()

# Calling the class method
Student.change_school_name("Cooperative University of Kenya")

print("\nAfter changing the school name:\n")
student1.display_info()
student2.display_info()
student3.display_info()