def even_odd(n):
    if n % 2 == 0:
        return True;
    else:
        return False;

num = int(input("Enter a number:"));
print(f"{num} is an {'even' if even_odd(num) else 'odd'} number.");