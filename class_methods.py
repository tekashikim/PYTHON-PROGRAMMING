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
        print("-" * 35)
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
student1 = Student("Hirum Kiarie", "CS001", "Computer Science")
student2 = Student("John Mwangi", "CS002", "Information Technology")
student3 = Student("Mary Wanjiku", "CS003", "Software Engineering")
print("Before changing the school name:\n")
student1.display_info()
student2.display_info()
student3.display_info()
Student.change_school_name("Cooperative University of Kenya")
print("\nAfter changing the school name:\n")
student1.display_info()
student2.display_info()
student3.display_info()