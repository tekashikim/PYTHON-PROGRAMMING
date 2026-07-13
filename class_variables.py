class Student:
    school_name = "The Cooperative University of Kenya"
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course
    def display_info(self):
        print("Student Details")
        print("Name:", self.name)
        print("Admission Number:", self.admission_number)
        print("Course:", self.course)
        print("School:", Student.school_name)
        print("-" * 30)
student1 = Student("Hirum Kiarie", "CS001", "Computer Science")
student2 = Student("Luke Mwangi", "CS002", "Information Technology")
student3 = Student("Mary Wanjiku", "CS003", "Software Engineering")
student1.display_info()
student2.display_info()
student3.display_info()
print("School Name (Accessed using the class):")
print(Student.school_name)
print("\nSchool Name (Accessed using objects):")
print(student1.school_name)
print(student2.school_name)
print(student3.school_name)