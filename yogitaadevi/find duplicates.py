def find_duplicates(words):
    new = set()
    duplicates = set()
    for word in words:
        if word in new:
            duplicates.add(word)
        else:
            new.add(word)

    return duplicates


word_list = list(map(str, input("Enter words: ").split()))
print(find_duplicates(word_list))
