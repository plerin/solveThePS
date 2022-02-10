'''
>> P
정사각형으로 이뤄진 섬과 바다가 있을 때 섬의 개수를 구하라
    - 가로/세로/대각선 연결 = 하나의 섬
    - w*h 크기 2차원 배열 
    - 1 : 땅 // 0 : 섬
    - 입력의 마지막 줄 0 0 이 주어짐 -> 반복 종료
>> S
connected component 유형인데 대각선까지 포함됨
1. 대각선을 어떻게 방향벡터로 표현할 것인가?
    - 방향벡터에 대각선 유형 추가 
'''
from collections import deque


def dfs(x: int, y: int):
    if graph[x][y] == 0:
        return False

    graph[x][y] = 0
    for i in range(len(dx)):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx and nx < h and 0 <= ny and ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)

    return True


def bfs(x: int, y: int):
    if graph[x][y] == 0:
        return False

    queue = deque([(x, y)])
    graph[x][y] = 0

    while queue:
        (x, y) = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx and nx < h and 0 <= ny and ny < w and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return True


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
    ans = 0

    for i in range(h):
        for j in range(w):
            if bfs(i, j):
                ans += 1

    print(ans)
