def count_characters_in_string():
    print("\nTask 1:")
    s = "hello world"
    print(f"Number of characters in {s}: {len(s)}")

def count_strings_with_same_start_end():
    print("\nTask 2:")
    strings = ["abc", "xyz", "aba", "1221"]
    count = sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])
    print(f"Count: {count}")

def first_last_two_chars_string():
    print("\nTask 3:")
    s = "python"
    if len(s) < 2:
        print(s)
    print(s[:2] + s[-2:])

def sort_tuples_by_last_element():
    print("\nTask 4:")
    tuples = [(1, 3), (3, 2), (2, 4)]
    for i in range(len(tuples)-1):
        for j in range(i+1, len(tuples)):
            if tuples[i][-1] < tuples[j][-1]:
                tuples[i], tuples[j] = tuples[j], tuples[i]
    print(tuples)

def add_ing_or_ly():
    print("\nTask 5:")
    s = "play"
    if len(s) < 3:
        result = s
    elif s.endswith("ing"):
        result = s + "ly"
    else:
        result = s + "ing"
    print(f"Result: {result}")

def generate_squares_list():
    print("\nTask 6:")
    print([x**2 for x in range(1, 21)])

def find_largest_and_smallest():
    print("\nTask 7:")
    nums = [5, 1, 9, 3, 7]
    largest = smallest = nums[0]
    for num in nums[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    print(f"Largest: {largest}, Smallest: {smallest}")

def common_elements_in_lists():
    print("\nTask 8:")
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print(set(list1) & set(list2))

def find_duplicate_words():
    print("\nTask 9:")
    words = ["apple", "banana", "apple", "cherry", "banana"]
    for i in set(words):
        if words.count(i) > 1:
            print(i)

def set_operations():
    print("\nTask 10:")
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

def sum_scores_by_name():
    print("\nTask 11:")
    tuples = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
    scores = {}
    for name, score in tuples:
        scores[name] = scores.get(name, 0) + score
    print(scores)

def word_length_dict_comprehension():
    print("\nTask 12:")
    words = ["hello", "world"]
    print({word: len(word) for word in words})

def double_tuple_elements():
    print("\nTask 13:")
    tup = (1, 2, 3)
    print(tuple(x * 2 for x in tup))

def swap_first_last_tuple():
    print("\nTask 14:")
    tup = (1, 2, 3, 4)
    lst = list(tup)
    lst[0], lst[-1] = lst[-1], lst[0]
    print(tuple(lst))

def merge_tuples_unique():
    print("\nTask 15:")
    tup1 = (1, 2, 3)
    tup2 = (3, 4, 5)
    print(tuple(set(tup1 + tup2)))

def main():
    count_characters_in_string()
    count_strings_with_same_start_end()
    first_last_two_chars_string()
    sort_tuples_by_last_element()
    add_ing_or_ly()
    generate_squares_list()
    find_largest_and_smallest()
    common_elements_in_lists()
    find_duplicate_words()
    set_operations()
    sum_scores_by_name()
    word_length_dict_comprehension()
    double_tuple_elements()
    swap_first_last_tuple()
    merge_tuples_unique()

if __name__ == "__main__":
    main()

