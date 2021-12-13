'''
>> P 
N*M에서 괴물을 피해서 탈출하는 최소 칸의 개수
    - (1,1) -> (N,M)
    - 그래프(2차원 배열)에서 최소 칸의 개수 == BFS
    - 0: 괴물 있어 / 1 : 괴물 없어
>> S
1. 상하좌우이동 -> 방향 벡터(dx,dy) 변수 선언 후 사용
2. bfs는 queue를 이용하니까 deque 사용
3. 1,1를 param으로 주고 queue에 담고 visit(list_graph 크기 & false로 초기화)
4. 방향벡터로 이동하며 1인경우 해당 위치 값 갱신(+1)
'''
from collections import deque


def bfs(x: int, y: int):
    global N, M

    queue = deque([(x, y)])

    while queue:
        (x, y) = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

bfs(0, 0)

print(graph[N-1][M-1])
