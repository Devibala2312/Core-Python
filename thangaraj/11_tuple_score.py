scores = [('John', 95), ('Jane', 87), ('Jim', 91), ('Jill', 82), ('John', 92), ('Jill', 90)]

consolidatedScores = {}

for name, score in scores:
    consolidatedScores[name] = consolidatedScores.get(name, 0) + score

print(consolidatedScores)

