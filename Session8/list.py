items = ['sport', 'LOL', 'BTS', 'Death note', 'Netflix']

l = len(items)
for i in range(l):
    print(items[i].upper())

for i, item in enumerate(items):
    print(i+1, ".", item.upper())

for i in items:
    char = list(i)
    for j in char:
        if j == "e" or j == "E":
            print(i)
