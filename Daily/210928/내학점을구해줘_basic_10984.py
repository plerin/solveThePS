

lst = [0,7,10,13,17,20,23,27,30,33,37,40,43]

t = int(input())
for _ in range(t):
    tot,avg = 0,0
    n = int(input())
    for _ in range(n):
        sco, gra = input().split()
        tot, avg = tot+int(sco),avg+float(gra)
    avg = avg / n * 10
    print(avg)
    for i in range(len(lst)):
        if avg < lst[i]:
            avg = lst[i]/10
            break
    # avg = lst[-1]/10
    
    print('{0} {1:.1f}'.format(tot,avg))