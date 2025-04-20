# 5. Write a Python program to add 'ing' to a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def conditional_append(ip):
    return ip if len(ip) < 3 else (ip+'ly' if ip.endswith('ing') else ip+'ing')
    
ip = 'testing'
print(conditional_append(ip))

ip = 'test'
print(conditional_append(ip))

ip = 'tes'
print(conditional_append(ip))

ip = 'te'
print(conditional_append(ip))
