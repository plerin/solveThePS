from collections import deque
# bfs


def bfs(s):
    lst = [s]
    queue = deque([s])

    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if i not in lst:
                lst.append(i)
                queue.append(i)

    return lst


# dfs
def dfs(s):
    visited.append(s)

    for i in sorted(graph[s]):
        if i not in visited:
            dfs(i)

    return visited

    # 입력 받기
N, M, S = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# print(' '.join(map(str, dfs(S))))
# print(' '.join(map(str, bfs(S))))
print(*dfs(S))
print(*bfs(S))
# ret
