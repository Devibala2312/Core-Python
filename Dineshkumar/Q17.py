#17. Write a program that finds the sum of all even numbers from 1 to 100 using a for loop

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total+=i

print(f"The sum of all even numbers from 1 to 100 is {total}")