# 1.Write a Python program to count the number of characters in a string.

# Input string
input = input("Enter a string: ")

char_count = {}

for char in input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
print("\nCharacter Occurrence Count:")

for key in char_count:
   print(f"'{key}': {char_count.get(key)}") 


# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

words = ["abc", "xyz", "aba", "1221", "aa", "a", "wow"]

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print(f"Number words with same first and last character: {count}")

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string

input = input("Enter a string: ")

if len(input) < 2:
    result = ""
else:
    result = input[:2] + input[-2:]

print(f"Result: {result}")
    
# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
  
word = input("Enter a string: ")

if len(word) < 3:
    result = word
elif (word.endswith("ing")):
    result = word[:-3] + "ly"
else:
    result = word + "ing"

print(f"Result: {result}")

# 6. Create a list comprehension that generates a list of squares of numbers from 1 to 20.
result = []

for i in range(1, 21):
    result.append(i**2)

print(f"Squares of numbers from 1 to 20: {result}")


# 7. Given a list of integers, find the largest and smallest numbers in the list without using the built-in max() and min() functions.

numbers = [3, 5, 1, 8, 2, 7]

for i in numbers:
    if i == numbers[0]:
        largest = i
        smallest = i
    elif i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")


# 8. Write a function that takes two lists and returns a set of elements that are common to both lists.

def common_elements(list1, list2):
    return set(list1) & set(list2)

print(f"Common elements {common_elements([1, 2, 3, 4, 5] , [4, 5, 6, 7, 8])}")

# 9. Given a list of words, return a set of words that appear more than once in the list.
words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
res_set = set()
for word in words:
    if words.count(word) > 1:
        res_set.add(word)

print(f"Words that appear more than once: {res_set}")

# 10. Given two sets, write a function to return their union, intersection, and difference.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1 | set2
intersection = set1 & set2
difference1 = set1 - set2
difference2 = set2 - set1
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"difference: {difference1}")
print(f"difference: {difference2}")


# 12. Create a dictionary comprehension that maps each word in a list to its length.
words = ["apple", "banana", "cherry"]
word_length_dict = {}

for word in words:
    word_length_dict[word] = len(word)

print(f"Word length dictionary: {word_length_dict}")

# 13. Write a function that takes a tuple of numbers and returns a new tuple with each element doubled

def double_tuple(tup):
    return tuple(i * 2 for i in tup)

print(f"Doubled tuple: {double_tuple((1, 2, 3, 4, 5))}")  

# 14. Write a function that swaps the first and last elements of a tuple.
def swap_tuple(tup):
    if len(tup) < 2:
        return tup
    return (tup[-1],) + tup[1:-1] + (tup[0],)
    
print(f"swap tuple{swap_tuple((1, 2, 3, 4, 5))}")

# 15. Write a function that takes two tuples and returns a new tuple that contains all elements from both tuples without any duplicates.

def remove_duplicates(tup1, tup2):
    combined = list(tup1) + list(tup2)
    return tuple(set(combined))

print(f"remove duplicates: {remove_duplicates((1, 2, 3), (3, 4, 5))}")


#16. Write a program to find the factorial of a number using a while loop.

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial(number)}")

#17. Write a program to find all the event numbers 0 to 100 using a for loop.

even_numbers = []
for i in range(0, 101, 2):
    even_numbers.append(i); 

print(f"Even numbers from 0 to 100: {even_numbers}")

#18. Write programs to count vowel in string.

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
print(f"Number of vowels in '{input_string}': {count_vowels(input_string)}")

#19. Write a program that takes a number and determines if it's even or odd using the modulus operator %

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#20 Write program to check person eligible to vote or not.

def check_voting_eligibility(age):
    if age >= 18:
        return True
    else:
        return False

age = int(input("Enter your age: "))
if check_voting_eligibility(age):
    print("You are eligible to vote.")
