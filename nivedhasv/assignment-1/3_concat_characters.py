# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string

def concat_string(ip):
    if len(ip) < 2:
        return ''
    return ip[:2]+ip[-2:]

ip= "hello python"
print(concat_string(ip))

ip= "he"
print(concat_string(ip))

ip= "h"
print(concat_string(ip))
