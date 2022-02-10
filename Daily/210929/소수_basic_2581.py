def prime(m,n):
    visited = [False for _ in range(n+1)]
    p = []

    for i in range(2,n+1):
        if visited[i] == True: continue
        p.append(i)
        for j in range(i*i,n+1,i):
            visited[j] = True
    p = list(filter(lambda x: m<=x and x<=n, p))
    return p

M = int(input())
N = int(input())

ret = prime(M,N)

if len(ret) == 0: print(-1)
else: print(sum(ret),min(ret),sep='\n')


# p = [i for in range(m,n+1) if i != 1 and all(i%j for j in range(2,i))]
# c = [i for i in range(a,b+1) if i != 1 and all(i % j for j in range(2,i))]  
# all(i%j for j in range(2,i)) --> 2부터 i(본인)까지 i%j 가 나누어 떨어지지않으면(0이 아니면) == 소수다 , 만약 0(False)가 하나라도 있으면 False 반환 