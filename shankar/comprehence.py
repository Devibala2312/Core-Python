input_string=[x  for x in range(1,3) ]
input_string1=[y for y in range(1,3) ]
print(input_string)
print(input_string1)
final_output=[x*y for x in input_string for y in input_string1]
print(final_output)