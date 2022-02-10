from collections import deque
# bfs 함수 명시


def bfs(i, j):
    q = deque([(i, j)])

    while q:
        a, b = q.popleft()
        for i in range(4):
            dn, dm = a+dx[i], b+dy[i]

            if dn < 0 or dn >= n or dm < 0 or dm >= m:
                continue
            if graph[dn][dm] == 0:
                continue
            if graph[dn][dm] == 1:
                graph[dn][dm] = graph[a][b]+1
                q.append((dn, dm))

    return graph[-1][-1]


ret = 0
graph = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 입력 받기
n, m = map(int, input().split())

# for _ in range(n):
#     graph.append(list(map(int, input())))

graph = [list(map(int, input())) for _ in range(n)]


# bfs 호출
ret = bfs(0, 0)

# 결과 출력
print(ret)
