'''
>> P
N*M 상자에 담김 토마토가 익는데 걸리는 최소 일수를 구하라
    - 익은 토마토의 상/하/좌/우에 있는 익지 않은 토마토는 하루 뒤에 익음
    - 익은 토마토(1) / 익지 않은 토마토(0) / 빈 칸(-1)
>> S
2차원 배열에서 최소 일자를 구하는 건 BFS
    - 준비물 : graph(list), dx/dy(list) _ 방향벡터, deque(library)
배열에 익은 토마토를 queue에 담아 놓아야 함
    - graph를 입력받을 때 값이 1인 경우(익은 토마토) queue에 담기
bfs 함수
    - param : queue(deque)
    - logic :
        1) while queue -> 방향벡터에 따른 값이 N*M안에 있는지 확인 후 0인 경우만 갱신
graph를 탐색하며 0이 있으면 -1 출력 없으면 그 중 가장 큰 값 출력
'''

from collections import deque


def bfs(queue: deque):
    global graph

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


M, N = map(int, input().split())
graph = []
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs(queue)
ans = 0
is_unripe = False

for row in graph:
    if 0 in row:
        is_unripe = True
    ans = max(ans, *row)

if is_unripe:
    print(-1)
else:
    print(ans-1)
