inputs = [-3, -2, 0, 1, 2, 4, 5, 7]
def yieldPositive(input):
    for i in input:
        if i > -1:
            yield i

generator = yieldPositive(inputs)

for num in generator:
    print(num)