import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    visited = [False]*(n+1)
    q = deque()
    q.append(s)
    ret = [1]
    visited[s] = True

    while q:
        start = q.popleft()
        for node in graph[start]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                ret.append(node)
    # print(ret)

    return ret


n = int(input())
graph = [[] for _ in range(n+1)]
# print(graph)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = list(map(int, input().split()))
order = [0]*(n+1)

for i in range(len(result)):
    order[result[i]] = i

print(order)

for i in range(1, len(graph)):
    graph[i].sort(key=lambda x: order[x])
print(graph)

ret = bfs(1)

if ret == result:
    print(1)
else:
    print(0)
