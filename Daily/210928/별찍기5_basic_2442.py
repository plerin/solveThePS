
n = int(input())
for i,v in enumerate(range(1,2*n,2)):
    print(' '*((n-1)-i)+'*'*v)