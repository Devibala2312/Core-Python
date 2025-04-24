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