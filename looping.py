# looping.py
# This program demonstrates the use of for and while loops.

# Example 1: Print numbers from 1 to 20
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i)


# Example 2: Multiplication table of a number entered by the user
number = int(input("\nEnter a number to display its multiplication table: "))

print(f"\nMultiplication Table of {number}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Example 3: Calculate the sum of numbers from 1 to 100 using a while loop
sum_numbers = 0
count = 1

while count <= 100:
    sum_numbers += count
    count += 1

print("\nSum of numbers from 1 to 100:", sum_numbers)


# Example 4: Print even numbers between 1 and 50
print("\nEven numbers from 1 to 50:")
for i in range(2, 51, 2):
    print(i)