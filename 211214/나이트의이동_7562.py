'''
>> P
나이트가 이동할 수 있는 칸이 주어졌을 때 a에서 b칸 최소 이동 횟수 구하라
    - 체스판은 정사각형(n*n)
>> S
그래프(2차원 배열)에서 최소 횟수 구하라
    -> BFS 풀이(DEQUE, dx/dy)
출발위치 -> 도착 위치 
    -> 비용이 따로 없으니 출발위치는 0으로 초기화 앞으로 도착위치 = 출발위치 값 + 1
'''

from collections import deque
import sys

input = sys.stdin.readline

MAX = 300


def bfs(sx: int, sy: int, ex: int, ey: int):
    queue = deque([(sx, sy)])
    graph[sx][sy] = 1

    while queue:
        x, y = queue.popleft()

        if x == ex and y == ey:
            print(graph[ex][ey]-1)
            return

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            # if nx < 0 or I <= nx or ny < 0 or I <= ny:
            #     continue
            # if graph[nx][ny] != 0:
            #     continue
            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(int(input())):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0] * I for _ in range(I)]

    bfs(start_x, start_y, end_x, end_y)
