
N,K = map(int,input().split())

ret = list(filter(lambda x: N%x == 0, range(1,N+1)))

if len(ret)>K:
    print(ret[K-1])
else:
    print(0)
# print((ret[K-1], 0)[len(ret)<=K])