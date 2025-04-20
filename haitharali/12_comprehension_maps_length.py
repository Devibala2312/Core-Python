# 12. Create a dictionary comprehension that maps each word in a list to its length.

def comprehension_maps_to_length(my_list):
    output_dict = {x: len(x) for x in my_list}
    print(output_dict)


comprehension_maps_to_length(["haithar", "ali"])
