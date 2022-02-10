'''
>> P
방향 없는 그래프에서 연결 요소 개수 구하기

>> S
1. N, M : 정점 개수와 간석 개수가 주어진다
2. 정점을 탐색하며 방문 체크(visited = True)하며 카운트 진행
3. 연결 요소 찾는건 dfs / bfs 방법으로 각각 함수 만들어 진행
    - dfs
    param : node(int) _ 현재 노드
    logic : visited = True 하고 인접 리스트를 탐색하며 visited = False 값만 진행
    - bfs  
    param : node(int) _ 출발 노드
    logic : deque에 넣고 인접 노드 중복 체크 하며 진행 
'''

from collections import deque
import sys

input = sys.stdin.readline


def dfs(node: int):
    global visited
    if visited[node] == True:
        return False

    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

    return True


def bfs(node: int):
    if visited[node] == True:
        return False

    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if dfs(i):
        ans += 1

print(ans)
