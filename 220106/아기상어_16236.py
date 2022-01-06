'''
>> P
N*N 크기 공간에 M마리 물고기를 1마리의 아기 상어가 먹을 수 있는 물고기를 전부 먹는데 걸리는 시간을 구하라
    - 초기값 : 아기 상어 크기는 2
    - 이동 : 자신보다 같거나 작은 물고기가 있거나 빈 칸인 경우만 상하좌우로만 이동 가능
    - 변동 : 가장 가까운 물고기를 먹으러 이동, (모두 거리가 같다면 맨위 그것도 같다면 가장 왼쪽)
            자신 크기와 같은 수 물고기를 먹을 때마다 크기가 1 증가 ex) 크기 2 -> 2마리 -> 크기 3 
>> S
조건이 많지만 2차원 배열 + 같은 가중치 + 최단 경로 이용 -> BFS
1. 본인보다 작은 물고기를 찾는다
    - 크기를 전역변수로 저장해두고 작은 순서대로 찾음(1~)
    1) 출발점에서 bfs 탐색으로 본인보다 작은 물고기 좌표 리스트 업
    2) 1개면 고 여러개면 위에있고 왼쪽에 있는 순서대로(x와 y가 작은것) 

먹이 대상을 우선순위 queue 사용하는거 어떰? 
    1) (x, y)로 x가 작은 순 그리고 x가 같으면 y가 작은 순 으로 뽑도록
    2) 먹이 대상이 끝나지 않을 때까지 bfs 탐색 그 때마다 start / end가 있는거지!

2. 최단경로로 이동한다(먹는다) + 먹은 카운트(진화를 위해) 의 반복 
    1) 이동하고 나서 visited or dist 초기화(누적_global)
    2) 먹은 물고기 개수 카운트(개수 맞으면 크기 +1)

정리
1. 입력 값을 받을 때 출발 좌표와 1인 좌표를 구함
    - 1인 좌표는 pray(우선순위 큐)에 저장
2. whlie pray: 하며 bfs(sx,xy) 호출
    - 먹이가 있을 때가지 반복하며 bfs()호출
    - bfs가 끝나면 결과값으로 좌표를반환하여 다음 bfs에 출발좌표로 사용
    - 9의 위치 변경

def bfs(x: int, y: int, dx: int, dy: int):
    global size, cnt
    dist = [[-1] * N for _ in N] 
    queue = deque(x,y)
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        
        if x == dx and y == dy:
            return dist[x][y]

        for dx, dy in move:
            nx, ny = ..

            if not isin(x,y) or arr[nx][ny] > size: continue

            if dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

하나를 놓쳤는데 우선순위 큐에서 꺼낼 때 (x,y) 뿐아니라 거리도 들어가야함
-> (크기, 거리, x, y)로 사용해야함 그래야 꺼낼 때 가장 크기가 작은 것 & 거리 가까운 것 & x가 작은거 & y가 작은거 순서대로 가져감



먹이가 있을 때 사냥한 후에 정렬을 해야 함
현재 위치에서 크기가 본인보다 작고 거리가 가까운 물고리를 선택하여 먹고 다시 정렬
prey에는 본인보다 작은 물고기가 있는데
    - 초기 값은 크기가 1인 물고기로 채운다
        -> prey.append((size, dist(0), x, y))
    - 정렬(size, dist 모두 작은 순)
        -> order(key=lambda a, b, c, d: (a,dist(x,y), x,y))
        -> 여기서 dist는 param(x,y)와 출발점(x,y)간 거리 반환 
    - 사냥
        -> bfs()돌며 출발점에서 도착점까지 거리 반환
        -> global ans += 
    - (옵션)상어 크기에 따라 먹이감 추가
        -> if cnt == size:
            cnt = 0 & size += 1 
    - 정렬(size, dist 모두 작은 순)
        -> sorted().popleft()

'''

from collections import deque
import sys
import heapq


input = sys.stdin.readline


def isin(x: int, y: int):
    if -1 < x < N and -1 < y < N:
        return True
    return False


def get_dist(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


def search(start: list, size: int):
    global prey
    # print([(x, y) for x in range(N)
    #    for y in range(N) if arr[x][y] == size - 1])
    for i in range(N):
        for j in range(N):
            if arr[i][j] == size-1:
                # dist = get_dist(start[0], start[1], i, j)
                prey.append((0, i, j))
                # heapq.heappush(prey, (arr[i][j], dist, i, j))


def bfs(sx: int, sy: int, ex: int, ey: int):
    global cnt
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    queue = deque([(sx, sy)])
    dist[sx][sy] = 0

    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            # print(sx, sy, dist[x][y])
            return dist[x][y]

        for dx, dy in move:
            nx, ny = dx + x, dy + y

            if not isin(nx, ny) or arr[nx][ny] > size:
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return 0


move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
arr = []
prey = []
start = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j]
            arr[i][j] = 0
        elif arr[i][j] == 1:
            prey.append((0, i, j))
            # dist = get_dist(start, (i, j))
            # heapq.heappush(prey, (arr[i][j], dist, i, j))
size = 2
cnt = 0
ans = 0

# prey_size, dist, dx, dy = sorted(prey, key=lambda x: (
#     x[0], get_dist(start[0], start[1], x[2], x[3]), x[2], x[3]), reverse=True).pop()
# print(prey_size, dist, dx, dy)
while prey:
    # 정렬
    prey.sort(key=lambda x: (
        get_dist(start[0], start[1], x[1], x[2]), x[1], x[2]), reverse=True)

    dist, dx, dy = prey.pop()
    print(start, dx, dy)
    ans += bfs(start[0], start[1], dx, dy)
    # print(dx, dy, ans, cnt, size, prey)
    start = [dx, dy]
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0
        # 먹이감 추가
        search(start, size)


print(ans)
