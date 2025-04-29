# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 08:35:23 2025

@author: sriram.balaji
"""

##Functional Programs


##Factorial of elements without duplicate.

def findFactorial(num: int):
    val: int =  num
    if num > 1:
        n = num - 1
        while n > 0:
            val = n * val
            n = n - 1
            
            
    return val
        
print('Factorial Value : ', findFactorial(5))


##Find sum of all even numbers from 1..100 using Loop

def findSumOfEvenNumbers(max_limit: int):
    sum_value: int = 0
    for i in range(0,max_limit, 2):
        sum_value = sum_value + i
        
    return sum_value

print('Sum upto 100 : ', findSumOfEvenNumbers(100))


##Count no of vowels using (IN) clause

def findVowelsInString(val: str):
    num_vow: int = 0
    for i in val:
        if i in ('a', 'e','i', 'o', 'u'):
            num_vow = num_vow + 1
            
    return num_vow

print('Number of vowels in words: ', findVowelsInString('Wovleasdf'))


##Find Odd / Even using modolus

def findOddOrEven(num_val: int):
    return 'Even' if num_val % 2 ==0 else 'Odd'

print('Odd or Even: ', findOddOrEven(10))


## Check whether a person can Vote  using logical operators


def checkVotingEligibility(age: int):
    return 'Can Vote' if age > 18 or age == 18 else 'Cannot Vote'


print('The user ', checkVotingEligibility(19))


##Yield positive integer

nums = [-3, -2, 0, 1, 2, 4, 5, 7]

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num


for positive in positive_numbers(nums):
    print(positive)

##Default arguments functions in Python

def welcomeUser(username: str = "Hola"):
    return f"Welcome {username}"

print(welcomeUser())
print(welcomeUser('Shiru'))


## Varargs in python

def sum_all(*args):
    return sum(args)


print(sum_all(1, 24, 36))
print(sum_all())


## kWarargs in python

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_user_info(name="Alice", age=30, country="Canada")
    
