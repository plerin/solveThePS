from collections import deque
# bfs


def bfs(s):
    lst = []
    queue = deque([s])

    while queue:
        v = queue.popleft()
        if v not in lst:
            lst.append(v)
        if len(lst) == N:
            break
        for i in graph[v]:
            queue.append(i)

    return lst


# dfs
def dfs(s, visited):
    visited.append(s)

    if len(visited) == N:
        return visited
    # print(visited)
    for i in sorted(graph[s]):
        if i not in visited:
            dfs(i, visited)

    return visited

    # 입력 받기
N, M, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
# visited = [False for _ in range(N+1)]
# visited = set()
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

print(str(dfs(S, []))[1:-1])
print(str(bfs(S))[1:-1])
# ret
