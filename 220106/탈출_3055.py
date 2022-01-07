'''
>> P
R*C 지도가 있을 때 S에서 D로 가는데 걸리는 최소 시간을 구하라
    - 빈 칸 = '.' // 물 = '*' // 출발점 = 'S' // 도착점 = 'D'
    - 이동은 상하좌우로 가능 // 물의 차오름도 상하좌우로 차오름
    - 물이 찰 예전인 칸으로 이동 못함
    - 도착 못하면 'KAKTUS'를 출력
>> S
고슴도치의 이동과 물의 차오름을 같이 고려해야 함
유형은 2차원 배열에서 같은 가중치 그리고 최단 경로로 BFS풀이
    - 고슴도치 이동 
        -> [nx][ny]가 '.'이고 방문하지 않았다면 방문 _ 기존 거리 + 1
        -> [x][y]가 '*'이면 continue:->queue에 담겨있더라도 
    - 물 이동
        -> [nx][ny]가 'D,X'가 아니고 방문하지 않았다면 방문
        -> 방문여부 체크를 어떻게 할 것인가? '.' -> '*'
같은 queue에 담아놓고 type으로 구분하되 고슴도치 이동 후 물 이동 순서대로 진행?

'''

from collections import deque
import sys

input = sys.stdin.readline


def isin(x: int, y: int):
    if -1 < x < R and -1 < y < C:
        return True
    return False

# 다음 좌표가 물이 차오를지 여부 확인


def check(x: int, y: int):
    for dx, dy in move:
        nx, ny = x + dx, y + dy

        if not isin(nx, ny):
            continue

        if arr[nx][ny] == '*':
            return False

    return True


def bfs():
    global queue, arr
    visited = [[False for _ in range(C)] for _ in range(R)]  # 방문 여부 체크

    while queue:
        x, y, dist, type = queue.popleft()

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if not isin(nx, ny) or arr[nx][ny] == 'X':  # 범위를 벗어나거나 돌을 만난 경우
                continue

            if type == DOCHI and not visited[nx][ny]:   # 고슴도치 이동
                if arr[nx][ny] == 'D':
                    return dist+1
                # 다음 좌표가 빈 칸 && 물이 차오르지 않는다면
                elif arr[nx][ny] == '.' and check(nx, ny):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1, type))
            elif type == WATER:
                if arr[nx][ny] == '.':  # 다음 좌표가 빈 칸인 경우
                    arr[nx][ny] = '*'
                    queue.append((nx, ny, dist, type))

    return 'KAKTUS'


R, C = map(int, input().split())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = []
queue = deque([])
start = ()

# 고슴도치와 물을 구분하기 위함
DOCHI = 1
WATER = 0

for i in range(R):
    row = list(input().rstrip())
    arr.append(row)
    for j in range(C):
        if arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == '*':
            queue.append((i, j, 0, WATER))

# 고슴도치 먼저 이동하기 때문에 queue 맨 앞에 추가
queue.appendleft((start[0], start[1], 0, DOCHI))
ans = bfs()

print(ans)
