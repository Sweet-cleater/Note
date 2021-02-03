import string
import random
print (''.join([string.printable[n] for n in [
 random.randint(0, 33) for r in range(20)]]))
 #33 = 1~9 + Alphabet 24