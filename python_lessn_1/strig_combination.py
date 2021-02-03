from functools import reduce
A = ['AA', 'AB', 'BB']
B = ['BA', 'BB', 'BC']

C = reduce(lambda x, y: x+y,[[(x,y) for y in B] for x in A])

print(C)
#A = ['AA', 'AB', 'BB'], B = ['BA', 'BB', 'BC']という書き方はダメみたい
#reduceのimportを追加