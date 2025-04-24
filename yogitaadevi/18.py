def vowel_count(a):
    count = 0
    for i in a:
        if i in 'aeiou':
            count+=1;
    return count;

a = input("Enter a string:");
print(vowel_count(a));
