student={"name":"Hirum Kiarie","age":20,"course":"Computer Science","grade":"A"}
print("Student Details:")
print(student)
print("\nName:",student["name"])
print("Age:",student["age"])
print("Course:",student["course"])
print("Grade:",student["grade"])
student["grade"]="A-"
student["age"]=19
print("\nUpdate Student Details:")
print(student)