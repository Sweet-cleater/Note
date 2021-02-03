from math import sqrt
for i in range(2,10000):
    if 0 not in [i%j for j in range(2, int(sqrt(i))+1)]:
        print (i)

#判定する数のルート以上の数は検証する不必要はない。