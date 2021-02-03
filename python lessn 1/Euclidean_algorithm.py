a, b = int(input()),int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print (gcd(a,b))
#解答はint()やprint()なかった　python2　の文ってことか。