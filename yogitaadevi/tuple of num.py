numbers = tuple(map(int, input("Enter numbers: ").split()))
print(tuple(a*2 for a in numbers))