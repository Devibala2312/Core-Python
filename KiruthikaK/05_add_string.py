input_String = "heading"
if len(input_String) > 3:
    input_String=input_String+'ly' if input_String[-3:]=='ing' else input_String+'ing'
print(input_String)

