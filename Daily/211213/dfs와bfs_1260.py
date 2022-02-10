'''
>> P
그래프를 dfs/bfs로 탐색한 결과 출력 
    - 정점 번호가 작은 것 부터 방문
    - 정점 번소는 1 ~ N까지다
>> S
1. N, M, V : 정점 개수, 간선 개수, 시작 정점이 주어진다
2. 두 정점이 주어지면 이를 통해 인접 정점을 변수로 초기화(양방향)
3. dfs / bfs 함수를 호출하여 결과 출력
'''
from collections import deque


def dfs(start: int):
    global visited

    visited[start] = True
    print(start, end=' ')

    for i in sorted(graph[start]):
        if not visited[i]:
            dfs(i)


def bfs(start: int):
    global visited

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
