name = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
result = {}
for nam, score in name:
    result[nam] = result.get(nam, 0)+score
print(result)
    