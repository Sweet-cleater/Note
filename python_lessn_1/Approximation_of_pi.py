import math
from numpy import random

N_in = 0
N_out = 0
N = 1000
x = random.rand(N)
y = random.rand(N)
r = x*x + y*y

for i in r:
    if i <= 1:
        N_in +=1
    else:
        N_out += 1

Pie = 4*N_in/N

print(Pie)

#別サイトを参考にした。