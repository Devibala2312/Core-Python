def set_operations(s1, s2):
    return {
        'union': s1 | s2,
        'intersection': s1 & s2,
        'difference_s1_minus_s2': s1 - s2,
        'difference_s2_minus_s1': s2 - s1
    }

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = set_operations(s1,s2)
print(result)
print(type(result))
print("Union:", result['union'])
print("Intersection:", result['intersection'])
print("s1 - s2:", result['difference_s1_minus_s2'])
print("s2 - s3:", result['difference_s2_minus_s1'])

