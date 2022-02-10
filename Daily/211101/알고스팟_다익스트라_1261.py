'''
[P]
N*M 미로가 있으며 (1,1)에서 (N,M)으로 이동하는데 최소 벽을 몇 개 부수어야 하는가?
    - 미로는 '0' : 빈 방  // '1' : 벽 으로 구성
    - N/M 의 범위는 1<=100
    - (1,1), (N,M)은 항상 뚫려있다.
    - 이동은 상/하/좌/우만 가능
[S]
N*M 그래프에서 최단 경로(여기선 벽의 최소 개수)
    1. 다익스트라 알고리즘 - 거리 비용 = 벽의 개수 ,, 출발지(1,1)에서 도착지(N,M)으로의 최단경로
    2. 그래프 탐색(BFS)
[L]
1. 입력 받기
    - M(int) : 열, N(INT) : 행
    - maze(list) : 미로를 그냥 받아 2차원배열 bfs 방식으로 -> 인접 노드 입력하는데 비용은 '0'/'1'여부
    - cost(list) : 비용 리스트로 INF 값으로 초기화
2. 다익스트라 준비물
    - 라이브러리 : heapq(우선 순위 큐)
    - 함수 : dijkstra(start)
3. 함수 선언
    - param :
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, start)
    cost[0][0] = 0
    while queue:
        c, x, y = heapq.heappop(queue)
        if cost[x][y] < c:
            continue

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            nc = c+graph[nx][ny]
            # try:
            #     nc = c+graph[nx][ny]
            # except IndexError as e:
            #     print(e, nx, ny)
            if nc < cost[nx][ny]:
                cost[nx][ny] = nc
                queue.append((nc, nx, ny))


M, N = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
cost = [[INF] * (M) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

dijkstra((0, 0, 0))

print(cost[N-1][M-1])
