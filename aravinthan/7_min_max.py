input = [3, 5, 8, 2, 1]

# Approach 1
input.sort()
print(f"Minimum - {input[0]}")
print(f"Maximum - {input[len(input)-1]}")

# Approach 2
def minimum(input):
    result = input[0]
    for i in range(1, len(input)):
        if input[i] < result:
            result = input[i]
    return result

print(f"Minimum - {minimum(input)}")

def maximum(input):
    result = input[0]
    for i in range(1, len(input)):
        if input[i] > result:
            result = input[i]
    return result

print(f"Maximum - {maximum(input)}")