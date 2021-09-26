from collections import deque


def bfs(i, j):
    cnt = 0
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for r in range(4):
            dn, dm = dx[r]+x, dy[r]+y

            if (0 <= dn and dn < len(graph)) and (0 <= dm and dm < len(graph)) and graph[dn][dm] == 1:
                cnt += 1
                graph[dn][dm] = 0  # 방문처리를 안 하면 무한루프에 빠져
                q.append((dn, dm))
    return max(cnt, 1)


# 입력 받기  한 줄 코드
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ret = []
# bfs 호출
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            ret.append(bfs(i, j))

# 결과 출력
print(len(ret))
print(*sorted(ret), sep='\n')
