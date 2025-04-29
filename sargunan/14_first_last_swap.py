# 14. Write a function that swaps the first and last elements of a tuple.

def swap(num):
    return (num[-1],) + num[1:-1] + (num[0],)

numbers = (1,2,3,4,5)
result = swap(numbers)
print(result)
