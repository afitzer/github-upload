# combining some code from count3 and words

name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Sort the dictionary by value
lst = list()
for k, v in list(counts.items()):
    lst.append((v, k))

lst.sort(reverse=True)

for k, v in lst[:30]:
    print(v, k)