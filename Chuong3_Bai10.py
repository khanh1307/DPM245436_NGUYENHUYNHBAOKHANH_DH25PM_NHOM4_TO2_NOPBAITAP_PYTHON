#CÃ¢u 10: TÃ­nh dÃ£y sá»‘
'''
'''
x = int(input("Nhá­p x: "))
n = int(input("Nhá­p N: "))
s = 0
for i in range(1, n + 1):
    tu = x**i
    mau = 1
    for j in range(1, i + 1):
        mau = mau * j
    s = s + (tu / mau)
print("s({0},{1})={2}".format(x, n, s))
