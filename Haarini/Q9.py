words = ["apple", "banana", "apple", "cherry", "banana"]
for i in set(words):
 if words.count(i) > 1:
    print(i)