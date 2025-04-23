def words_length(words_list):
    words_dict = {word: len(word) for word in words_list}
    return words_dict

word_list=input("Enter the list of words (separated by comma): ")
word_list = [word.strip().lower() for word in word_list.split(",")]
print("Words and length", words_length(word_list))
