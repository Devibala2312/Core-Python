text = 'google.com'
d = {}
for i in text:
    d[i] = d.get(i,0)+1
print(d)