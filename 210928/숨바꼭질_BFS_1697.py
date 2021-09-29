
'''
BFS로 돌면서 VISIT에 없으면 Q.APPEND(N-1,N+1,2N)할 꺼야 
VISIT은 LIST인데 안의 내용은 (N,COST)로 저장할꺼 
그럼 N1 IN VISIT의 N리스트에 있는지 어떻게 확인해 ? 
'''
from collections import deque
def bfs(n,k):
    q = deque([(n,0)])

    while q:
        v = q.popleft()
        
        if v[0] < 0 or v[0] > 100000: continue
        if v[0] in visit2: 
            print('gg',v[0])
            continue
        if v[0] == k: return v[1]

        visit2.append(v[0])
        
        q.append((v[0]-1,v[1]+1))
        q.append((v[0]+1,v[1]+1))
        q.append((v[0]*2,v[1]+1))
    

N, K = map(int, input().split())

visit1 = []
visit2 = []

ret = bfs(N,K)
print(ret)