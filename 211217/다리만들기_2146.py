'''
>> P
N*N 대륙에서 길이가 가장 짧은 다리를 놓을 때의 길이 출력
    - 섬 = 동서남북으로 육지가 붙어있는 덩어리
>> S
여러 섬이 있는데 가장 길이가 짧은 다리를 구하라 
    - 2차원 배열에서 가장 짧은 다리
    -> BFS
바다와 맞닿아있는 육지에서 모두 BFS를 통해 육지를 구하고 그 중 가장 짧은 값 리턴
    - 같은 섬인 경우는 제외 => 같은 섬인 표시를 남겨두면 좋겠다
    - 육지를(다른 섬) 만나는 순간 BFS 탐색 OFF
같은 섬끼리 표시 남기고 바다와 맞닿은 경우 체크
    - connected_component하며 같은 섬은 표시하고 바다와 맞닿은 경우 리스트에 담기
    - 바다와 맞닿은 경우만 반복하며 다른 섬까지 길이 체크 
    -> 함수가 2개 필요

>> F
find_island(start:int)
    - logic :
        1) global cnt(int) _ island classify 
        2) search with direction_vector(dx/dy) -> if 0 -> fillwith  cnt
    - return : True/False -> if True then it's found the island -> True
shortest_route(x:int, y:int, island:int)
    - vari : global dist = [0] * (N)
    - logic :
        1) for i in graph[now] -> if dist[i] == 0 -> dist[i] = dist[now]+1
        2) if graph[x][y] != island and graph[x][y] != 0 then return dist[x][y]
    -> ans = min(ans, ret)

풀이보고 다시 짜보자
1. 같은 섬음 묶어주는 역할하는 bfs1
    - visit(false/true)와 cnt(섬을 구분하기 위한 수)
    -> 결과는 visit이 모든 elem를 true로 하면서 섬인 elem은 1이상의 값으로 갱신
2. 섬에서 다른 섬까지 가장 짧은 길이를 구하는 bfs2가 필요해
    - 각 섬에서 다른 섬까지의 길이를 구하기위해 섬 개수(1~count)만큼 반복하며 call
    - dist를 N*N 크기로 -1로 초기화, 해당 graph에서 count를 갖는 부분은 0으로 초가회
    - 방향벡터로 이동하며 섬이 아닌 부분 필터링 + grapn[nx][ny] > 0 이고 cnt와 다르면 ans 갱신
    - graph[nx][ny] == 0 and dist[nx][ny] == 1이면 탐색 
이 문제 풀이에 핵심은 
입력 받은 그래프를 같은 섬별로 갱신하고
섬에서 다른 섬으로 길이 구하는 건 섬만큼 반복하며 거리는 모두 각자 초기화하여
graph와 dist를 섞어서 사용한다는 것!!! 
'''

from collections import deque
import sys

input = sys.stdin.readline


def bfs1(x: int, y: int):
    global visit

    queue = deque([(x, y)])
    visit[x][y] = True
    graph[x][y] = count
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] == 1:
                visit[nx][ny] = True
                graph[nx][ny] = count
                queue.append((nx, ny))


def bfs2(z: int):
    global ans
    # dist는 bsf2 부를 때마다 -1로 초기화하므로 걱정 없어
    dist = [[-1] * N for _ in range(N)]
    queue = deque([])

    for i in range(N):
        for j in range(N):
            if graph[i][j] == z:
                dist[i][j] = 0
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            elif graph[nx][ny] > 0 and graph[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return
            elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 1
ans = sys.maxsize

for i in range(N):
    for j in range(N):
        if not visit[i][j] and graph[i][j] == 1:
            bfs1(i, j)
            count += 1

for row in graph:
    print(*row)

# 섬 개수(1~count)만큼 반복
for i in range(1, count):
    bfs2(i)

print(ans)
