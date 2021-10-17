'''
일반식 : dn = dn-1 +(n-1)x6 (d1 = 2)
'''
N = int(input())

if N == 1:
    print(1)
else:
    layer_idx = [2]
    n = 1
    while N >= layer_idx[n-1]+(n-1)*6:
        layer_idx.append(layer_idx[n-1]+(n-1)*6)
        n += 1

    print(n)


a = int(input())
c = 1
while a > 1:
    a = a-6*c
    c += 1
print(c)
