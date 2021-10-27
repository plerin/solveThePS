'''
[P]
N*M*H 크기의 토마토 상자가 있어 모든 토마토가 익는데 걸리는 일자 출력
    - 0 : 익지 않은 토마토 // 1 : 익은 토마토 // -1 : 토마토가 들어있지 않음
    - 익은 토마토 상/하/좌/우/위/아래의 토마토가 1일 후에 익어
    - 결과 0(처음부터 모두 익음), -1(모두 익지 못함), N(익는데 걸리는 시간)
[S]
익는데 걸리는 최소 시간 == BFS(토마토가 다른 토마토에 영향을 주는 시간은 '1'일로 동일해)
    - 방향벡터를 이용해 상/하/좌/우/위/아래 방문체크
    - 시작 지점은 상자안에 있는 모든 익은 토마토
[L]
1. 위/아래를 어떻게 구조화할 것인가?
    - 3차원 배열로 GRAPH 구성
    - 방향 벡터 : dx/dy/dz 로 [z, -z, x, -x, y, -y]
2. 방문 체크
    - elem 이 '0'인 것을 방문해서 '1'로 방문체크
'''

from collections import deque
import sys
input = sys.stdin.readline


def ripenDay(v):
    q = deque([v])

    while q:
        z, x, y = q.popleft()

        for i in range(len(dx)):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]

            if nz < 0 or nz >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                cost[nz][nx][ny] = 1 + cost[z][x][y]
                q.append((nz, nx, ny))


M, N, H = map(int, input().split())
graph = []
cost = [[[0] * M for _ in range(N)] for _ in range(H)]
dx, dy, dz = [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1], [1, -1, 0, 0, 0, 0]

for _ in range(H):
    graph.append([list(map(int, input().split())) for _ in range(N)])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                ripenDay((i, j, k))
ret = True
max_day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                ret = False
            max_day = max(max_day, cost[i][j][k])

if ret == True:
    print(max_day)
else:
    print(-1)
