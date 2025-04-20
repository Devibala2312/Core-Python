word_list=input("Enter the list of words (separated by comma): ")
word_list = [word.strip().lower() for word in word_list.split(",")]
element_count={}
for word in word_list:
    if word in element_count:
        element_count[word] += 1
    else:
        element_count[word] = 1
for key, value in element_count.items():
    if value > 1:
        print(f"{key} - {value}")
