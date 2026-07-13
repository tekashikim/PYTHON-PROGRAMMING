print("Numbers from 1 to 20:")
for i in range(1,21):
    print(i)
number=int(input("\nEnter a number to display its multiplication table:"))
print(f"\nMultiplication Table of{number}")
for i in range(1,11):
    print(f"{number}*{i}={number*1}")
sum_numbers=0
count=1
while count<=100:
    sum_numbers+=count
    count+=1
print("\nSum of numbers from 1 to 100:",sum_numbers)
print("\nEven numbers from 1 to 50:")
for i in range(2,51,2):
    print(i)