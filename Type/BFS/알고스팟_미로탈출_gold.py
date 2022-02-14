'''
backjoon url -> https://www.acmicpc.net/problem/1261

>> Keyword
BFS, 우선순위 큐(heapq)
여러 루트가 있을 때 시간 소요를 최소화 하기 위해 특정 조건을 우선 탐색
heapq : 기본적으로 최소 값, 최대 값을 구하고 싶으면 '-'를 붙임

>> P
N*M 미로에 갇혔다. 방 크기는 1*1로 이루어져 있으며 
빈 방은 자유롭게 다닐 수 있지만 벽은 부수지 않으면 이동 불가
상하좌우로만 이동 가능할 때 (1,1) -> (N, M)으로 이동하는데 벽을 최소 몇 개 부수어야 하는가?

>> S
2차원 배열에서 미로 탈출(비용도 같아) -> BFS
이 문제는 최소 이동 비용이 아닌 최소 벽 부수는 개수를 구해야함

여러 루트 중 벽을 최소한으로 만나는 방법으로 가야하는데 
여러 루트 중! 최소한! -> 우선순위 큐(heapq)
균등하게 찾으면 시간초과 에러 발생


'''
from collections import deque
import sys
import heapq

input = sys.stdin.readline


def solve(x: int, y: int, wall: int) -> int:
    queue = []
    # 우선순위 큐 우선순위를 벽을 만난 횟수
    heapq.heappush(queue, (wall, x, y))

    while queue:
        wall, x, y = heapq.heappop(queue)

        # 벽을 만난 최소 횟수부터 구하니까 목적지 도착 == 벽 만난 최소 횟수
        if x == N-1 and y == M-1:
            return wall

        for dx, dy in move:
            nx, ny = x+dx, y+dy
            # 범위에 포함되며 첫 방문인 경우!
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                # 비용(벽 만난 횟수) 갱신 = 기존 횟수 + 현재 벽 여부
                dist[nx][ny] = wall + maze[nx][ny]
                heapq.heappush(queue, (dist[nx][ny], nx, ny))


M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

# elem오기까지 벽 만난 최소 횟수 저장(벽 부숨)
dist = [[-1] * M for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(solve(0, 0, 0))
