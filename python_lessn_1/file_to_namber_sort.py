a = open('text.text').read().split()
a.sort()
for i in a[::-1]:
    print(i)