MAX = 10000
List = range(MAX + 1)
#Eratosthenesの方はこの書き方注意されるけど　こっちうごく何で？
for i in range(2, int(MAX ** 0.5)):
    List = [x for x in List if (x == i or x % i != 0)]
    for j in List:
        print(j)
#サイトにはver1よりver2の方がはやいって書いてたけど、俺の環境やと明らかに、ver2の方が遅い