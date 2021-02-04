import random

with open('out.txt') as f:
    l = f.readlines()

l = [s for s in l if s != '\n']

while(1):
    content1 = random.randrange(len(l))
    content2 = random.randrange(len(l))
    if content1 != content2:
        break

print(l[content1] + l[content2])