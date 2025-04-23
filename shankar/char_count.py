from collections import Counter


def char_count(input_string):
    char_count=Counter(input_string)

    for char, count in char_count.items():
        print(f"Character {char} is {count}")



input_string="shankar"
char_count(input_string)
