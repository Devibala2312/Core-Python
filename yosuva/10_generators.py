# Create a generator that yields only even numbers from 1 to 10

def even_gen():
    for x in range(1, 11):
        if x % 2 == 0:
            yield x

for num in even_gen():
    print(num)