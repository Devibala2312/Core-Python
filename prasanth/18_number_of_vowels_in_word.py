def vowels_in_word(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = sum(1 for char in word if char in vowels)
    return count

input_word = input("Enter the word to find number of vowels:")
print("Number of vowels in word: ", vowels_in_word(input_word))
