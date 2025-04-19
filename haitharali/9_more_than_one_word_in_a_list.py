# 9. Given a list of words, return a set of words that appear more than once in the list.

def more_than_one_time(input_list):
    output_list = []
    length = len(input_list)
    for i in range(length):
        for j in range(i + 1, length):
            if input_list[i].lower() == input_list[j].lower():
                output_list.append(input_list[i])
                break
    print("output list ", output_list)


more_than_one_time(["abc", "xyx", "abc", "bcd", "xyz", "xyz", "123", "BCD"])
