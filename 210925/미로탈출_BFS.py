from collections import deque


def bfs(i, j):
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dn = x + dx[i]
            dm = y + dy[i]

            if dn < 0 or dn >= n or dm < 0 or dm >= m:
                continue
            if graph[dn][dm] == 0:
                continue
            if graph[dn][dm] == 1:
                graph[dn][dm] = graph[x][y]+1
                queue.append((dn, dm))
    return graph[n-1][m-1]


n, m = map(int, input().split())
graph = []
ret = 0

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ret = bfs(0, 0)

print(ret)
