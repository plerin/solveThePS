
t = int(input())
for _ in range(t):
    tot,avg = 0,0
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        tot,avg = tot+int(a),avg+float(b)
    print('{0} {1:.1f}'.format(tot,avg/n))