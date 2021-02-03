List = list(range(10000))
#python2　List = range(10000)　の書き方はできない
#しかし、どうやらそこが問題ではなく、このしたの  List[1] = 0 と一緒に使うと問題だった。
List[1] = 0 #1は素数ではない
for p in List:
    if not p:
        continue
    elif p > 100: #1000 ** 0.5
        break
    else:
        for multi in range(p+p, 10000, p): #解答では、xrange　になっているが、range　にすれば良い
            List[multi] = 0


List = [x for x in List if x]
for x in List:
    print(x)

#This is certainly faster than the other code, and I can get structure of list.