#17. Write a program that finds the
# sum of all even numbers from 1 to 100 using a for loop

sum_even = sum([num for num in range(1, 101) if num % 2 == 0])
print("The sum of all even numbers from 1 to 100 is:", sum_even)

