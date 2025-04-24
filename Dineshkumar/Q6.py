#6. Create a list comprehension that generates a list of squares of numbers from 1 to 20.

list = []
for number in range (1, 21):
    value = number ** 2
    list.append(value)
print(list)

