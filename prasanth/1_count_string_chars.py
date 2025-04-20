from collections import Counter

print("Program to count the number of characters in a string")
string = input("Enter your string: ")
string = string.lower()
strCount = {}
for v in string:
    strCount[v] = strCount.get(v,0) + 1
print("The character counts are (using for loop)", strCount)
count = Counter(string)
print ("The character counts are(using counter collection) ", dict(count))