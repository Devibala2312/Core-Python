def get_postive_num(numbers):
    for i in numbers:
        if i > 0:
            yield i
numbers = list(map(int, input("Enter a list of numbers:").split()));
pos_numbers = get_postive_num(numbers);
for i in pos_numbers:
    print(i);