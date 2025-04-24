items = list(map(str, input("Enter the list of items: ").split()))
result_dict = {item:len(item) for item in items }
print(result_dict)