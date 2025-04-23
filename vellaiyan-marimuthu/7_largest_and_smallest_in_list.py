list = input("Enter the list of numbers to find min and max(separated by comma): ")
numbers = [word.strip() for word in list.split(",")]
numbers.sort()
print(f"The minimum number is {numbers[0]} and maximum number is {numbers[-1]} (using sort function)", )
maximum=numbers[0]
minimum=numbers[0]
for num in numbers:
    if num<minimum:
        minimum=num
    if num>maximum:
        maximum=num
print(f"The minimum number is {minimum} and maximum number is {maximum} (using loop)", )