#1.Write a Python program to count the number of characters in a string.
def program():

    input = 'google.com'
    count = {}
    for char in input:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    print(f'input :: {input}')
    print(f'count :: {count}')

program()

#2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def program():
    Sample_List = ['abc', 'xyz', 'aba', '1221']
    result = []
    for str in Sample_List:
        if len(str) >= 2:
            if str[0] == str[-1]:
                result.append(str)

    print(f'input :: {Sample_List}')
    print(f'count :: {result}')

program()

#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string

def program():
    input = 'ki'
    result = ''
    if len(input) > 1:
        result = input[:2]+input[-2:]

    print(f'input :: {input}')
    print(f'count :: {result}')

program()

#4 .Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def program():
    input = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result = sorted(input, key=get_last_element)
    print(f'input :: {input}')
    print(f'result :: {result}')

def get_last_element(t):
    return t[-1]

program()

#6. Create a list comprehension that generates a list of squares of numbers from 1 to 20.

def program():
    squares = [x**2 for x in range(1, 21)]
    print(f'result :: {squares}')

program()

#7. Given a list of integers, find the largest and smallest numbers in the list without using the built-in max() and min() functions.

def program():
    numbers = [1, 2, 5, 4, 7, 9, 34, 54, 3]
    min = max = numbers[0]
    for num in numbers:
        if num <= min:
            min = num
        if num >= max:
            max = num

    print(f'min :: {min}')
    print(f'max :: {max}')

program()

#8. Write a function that takes two lists and returns a set of elements that are common to both lists.

def program():
    list1 = [1, 2, 5, 4, 7, 9, 34, 54, 3]
    list2 = [5, 6, 9, 3, 1, 65]
    common = []
    for num in list1:
        for number in list2:
            if (num == number):
                common.append(num)

    print(f'common :: {common}')

program()

#9. Given a list of words, return a set of words that appear more than once in the list.

def program():
    names = ['java', 'python', 'nodejs', 'java', 'aws', 'aws']
    duplicate = {}
    result = []
    for name in names:
        if name in duplicate:
            result.append(name)
        else:
            duplicate[name] = True

    print(f'result :: {result}')

program()


# 10. Given two sets, write a function to return their union, intersection, and difference.
def program():
    s1 = {1, 3, 5, 7, 9, 2}
    s2 = {3, 5, 6, 7, 8}

    print(f'union :: {s1 | s2}')
    print(f'intersection :: {s1 & s2}')
    print(f'difference s1:: {s1 - s2}')
    print(f'difference s2:: {s2 - s1}')


program()


# 11. Given a list of tuples where each tuple contains a name and a score (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)]), write a function to return a dictionary where each name maps to the sum of their scores.
def program():
    t = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
    result = {}

    for name, score in t:
        if name in result:
            result[name] += score
        else:
            result[name] = score

    print(f'name :: {result}')


program()

# 12. Create a dictionary comprehension that maps each word in a list to its length.
fruits = ['apple', 'mango', 'orange', 'grapes', 'guva', 'kiwi']
dic = {fruit: len(fruit) for fruit in fruits}
print(f'dic :: {dic}')

# 13. Write a function that takes a tuple of numbers and returns a new tuple with each element doubled
numbers = (1, 2, 3, 4, 5)
doubled = tuple(num * 2 for num in numbers)
print(f'dic :: {doubled}')

# 14. Write a function that swaps the first and last elements of a tuple.


def get_swap_first_last(num):
    if len(num) < 2:
        return num
    else:
        return (num[-1],) + num[1:-1] + (num[0],)


numbers = (1, 2, 3, 4, 5)
print(f'get_swap_first_last :: {get_swap_first_last(numbers)}')

# 15. Write a function that takes two tuples and returns a new tuple that contains all elements from both tuples without any duplicates.

t1 = (1, 2, 3, 4, 5)
t2 = (2, 3, 6, 7)


def get_combined_unique_tuple(t1, t2):
    combined_tuple = set(t1 + t2)
    return combined_tuple


print(f'get combined tuple :: {get_combined_unique_tuple(t1, t2)}')

# 16. Write a program to find the factorial of a number using a while loop.

num = 5
result = 1
while num > 1:
    result *= num
    num -= 1
print(f'factorial of a number :: {result}')

# 17. Write a program that finds the sum of all even numbers from 1 to 100 using a for loop

result = sum(x for x in range(1, 101) if x % 2 == 0)
print(f'The sum of all even numbers :: {result}')


# 18. Write a program to count the number of vowels in a string using membership operators (in)

def count_the_number_of_vowels(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in input:
        if ch in vowels:
            count += 1
    return count


print(f'count the number of vowels :: {count_the_number_of_vowels('programming')}')


# 19. Write a program that takes a number and determines if it's even or odd using the modulus operator %

def odd_or_even(num):
    if num % 2 == 0:
        return 'even'
    return 'odd'


print(f'even or odd :: {odd_or_even(1)}')


# 20. Write a program to check whether a person can vote (age >= 18) using logical operators

def eligible_to_vote(num):
    return num > 18


print(f'eligible_to_vote :: {eligible_to_vote(5)}')


# 21. Write a program to yield positive number from the given listing using python generator

def yield_positive_num(nums):
    for num in nums:
        if num > 0:
            yield num


nums = [-3, -2, 0, 1, 2, 4, 5, 7]
print(f'eligible_to_vote :: {list(yield_positive_num(nums))}')


# "22. Write a function name 'welcome' that prints a welcome message for the user using default argument,
# if user name provided that shoult print user name, otherwise default name should be printed"

def greeting(name="spider"):
    return (f'Welcome {name}')


print(f'Greeting :: {greeting('Groot')}')


# 23. Write a function sum_all(*args) that accepts any number of numeric arguments and returns their sum.

def sum_all(*args):
    return sum(args)


print(f'Greeting :: {sum_all(1, 2, 3)}')


# "24. Write a function print_user_info(**kwargs) that accepts any number of keyword arguments and
# prints them in key: value format."

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_user_info(name="Alice", age=25, city="NYC")

# "25. Scopes - local & global"

visits = 0


def track_visit(page):
    global visits
    visits += 1
    print(f'User visited {page} .Total visits:{visits}')


track_visit("Home")
track_visit("About")