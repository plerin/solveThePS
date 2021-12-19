'''
>> S
1. 인접한 육지를 이어서 섬으로 묶는다.
    -> DFS 방식으로 connected_component 풀이
    -> 1~N으로 섬을 같은 숫자로 묶는다.
        - 필요 : visit:list -> False , dx/dy, count:int(global)
        - 모든 좌표에서 실행 (visit-> False인경우만)
2. 섬에서 다른 섬으로 최단 거리를 구한다.
    -> A->B 서로 다른 섬으로 가는데 최소 값을 구한다.
    -> global ans = sys.maxsize() -> 최소 값으로 갱신한다.
        - need : deque(library), dx/dy, dist(list), ans(int,global)
        - 섬 개수만큼 반복
'''

from collections import deque
import sys

input = sys.stdin.readline


def gather_island(x: int, y: int):
    global visit
    visit[x][y] = True
    graph[x][y] = count
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] != 0:
            gather_island(nx, ny)


def short_route(island: int):
    global ans

    dist = [[-1] * N for i in range(N)]
    queue = deque([])
    for i in range(N):
        for j in range(N):
            if graph[i][j] == island:
                dist[i][j] = 0
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
            elif graph[nx][ny] != island and graph[nx][ny] != 0:
                ans = min(ans, dist[x][y])
                return

    # queue = deque([island])


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 1

for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] != 0:
            gather_island(i, j)
            count += 1

ans = sys.maxsize

for i in range(1, count):
    short_route(i)

print(ans)
# for row in graph:
#     print(*row)
