age=20
if age>=18:
    print("You are allowed to vote.")
score=int(input("\nEnter student's score:"))
if score>=50:
    print("Student passed.")
else:
    print("Student failed.")
num=int(input("\nEnter a number to check even or odd:"))
if num %2==0:
    print("The number is even.")
else:
    print("The number is odd.")
print("\nFind the largest of three numbers")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print("Largest number is:",largest)