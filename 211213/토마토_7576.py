'''
>> P
N*M 상자에 담긴 토마토가 모두 익는 최소 일수 구하라
    - 1 : 익은 토마토   // 0 : 익지 않은 토마토 // -1 : 토마토 없는 칸
    - 익은 토마토의 상하좌우의 토마토는 하루 지나면 익어(0->1)
    - 모두 익지 못하는 상황에는 -1 반환
>> S
1. N*M 그래프에서 최소 일수 구하라 ==> BFS
2. n*m 탐색하며 1인경우 주변 토마토 익도록 시켜 ==> BFS 함수 호출
3. 결과 출력에서 GRAPH에 0이 있다면 -1 없다면 가장 큰 값 리턴
'''
from collections import deque
import sys

input = sys.stdin.readline


def bfs(x: int, y: int):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or N <= nx or ny < 0 or M <= ny:
                continue
            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0 or graph[x][y] + 1 < graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

            # if (0 <= nx and nx < N and 0 <= ny and ny < M) and graph[nx][ny] >= 0:
            #     if graph[nx][ny] == 0 or graph[x][y] + 1 < graph[nx][ny]:
            #         queue.append((nx, ny))
            #         graph[nx][ny] = graph[x][y] + 1

            # if (0 <= nx and nx < N and 0 <= ny and ny < M) and (graph[nx][ny] == 0 or graph[x][y] + 1 < graph[nx][ny]):
                # if nx < 0 or N <= nx or ny < 0 or M <= ny:
                #     continue
                # elif graph[nx][ny] == -1:
                #     continue
                # elif graph[nx][ny] == 0 or graph[x][y] + 1 < graph[nx][ny]:


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
is_unripe = False
ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j)

for row in graph:
    if 0 in row:
        is_unripe = True
    ans = max(ans, *row)

if is_unripe == True:
    print(-1)
else:
    print(ans-1)
