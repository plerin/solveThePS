from collections import deque
def bfs(s,e):
    q = deque([s])
    cnt = 0
    while q:
        v = q.popleft()

        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                q.append(i)
        cnt+=1


# 입력 받기
n = int(input())
a, b = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = []
ret = 0

for _ in range(int(input())):
    p, c = map(int,input())
    graph[p].append(c)
    graph[c].append(p)

# bfs 호출
ret = bfs(a,b)

# 결과 리턴
print(ret)