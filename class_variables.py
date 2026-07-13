# class_variables.py
# This program demonstrates the use of class variables in Python.

# Creating a class
class Student:
    # Class variable (shared by all objects)
    school_name = "The Cooperative University of Kenya"

    # Constructor
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    # Method to display student details
    def display_info(self):
        print("Student Details")
        print("Name:", self.name)
        print("Admission Number:", self.admission_number)
        print("Course:", self.course)
        print("School:", Student.school_name)
        print("-" * 35)


# Creating Student objects
student1 = Student("Hirum Kiarie", "CS001", "Computer Science")
student2 = Student("John Mwangi", "CS002", "Information Technology")
student3 = Student("Mary Wanjiku", "CS003", "Software Engineering")

# Displaying information
student1.display_info()
student2.display_info()
student3.display_info()

# Accessing the class variable directly
print("School Name (Accessed using the class):")
print(Student.school_name)

# Accessing the class variable through objects
print("\nSchool Name (Accessed using objects):")
print(student1.school_name)
print(student2.school_name)
print(student3.school_name)