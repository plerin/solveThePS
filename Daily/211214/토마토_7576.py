'''
>> P 
N*M 상자안에 토마토가 들어가있는데 모두 익을 때 걸리는 최소 시간 찾아라
    - 1 : 익은 // 0 : 안익은 // -1 : 빈 칸
    - 익은 토마토 상하좌우로 안 익은 토마토가 하루만에 익어
    - 모두 익지 못하는 상황이면 -1 출력
    - N*M은 모두 ~1000까지
>> S
2차원 배열안에 최소 일자 구하기
    - BFS(DEQUE, 방향벡터 이용한 풀이)
N,M 범위가 ~1000
    - 일반적인 풀이로 시간초과 나올 가능성 높아
    - 익은 토마토([x][y] = 1)가 있는 자리를 기억해 그것만 반복하자
최소 일자를 구해야하니까 만약 이미 익었다고 해도 값이 더 작다면 갱신

++
이 문제에 놓쳤던 부분
queue는 선입선출인데 queue에 익은 토마토를 곧바로 넣어주면
(0,0)자리의 토마토 다음 처리되는 토마토가 (1,0)이 아닌 (3,5)가 되므로 
[nx][ny]가 [x][y]+1보다 큰 경우를 안 따져도 된다.!

'''

from collections import deque


def bfs(queue: deque):
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


M, N = map(int, input().split())
graph = []
queue = deque()
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

bfs(queue)

is_unripe = False
ans = 0

for row in graph:
    if 0 in row:
        is_unripe = True
    ans = max(ans, *row)

if is_unripe == True:
    print(-1)
else:
    print(ans-1)
