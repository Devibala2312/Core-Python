def positive_numbers(numberList):
    for num in numberList:
        if num > 0:
            yield num

print("The positive numbers are: ", list(positive_numbers([-10,4,5,6,-9])))