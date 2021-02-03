def fib():
    a = b = 1
    while True:
        yield a
        a, b = b, a+b

f = fib()
print("フィボナッチ数列を第N項まで計算します。:")
N = int(input())
for t in range(N):
    print (f.__next__(),)
#xrange -> range f.next() -> f.__next__()