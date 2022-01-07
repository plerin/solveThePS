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


# 아 지금 나는 좌표간 거리를 (x1,y1), (x2,y2)에서 맨해튼 거리로 구하는데
# 실제로 값에 따라서 그렇지 못한 경우가 있을 수 있구나!!!
'''
그 사이에 내가 지나가지 못하는 물고기가 있으면 그 거리는 맞지 않는거니까!!
그러니까 bfs 구할 때 최단경로를 구하니까 그 경로로 가자
1. bfs 반복문은 while True:
2. 도착점은 조건(범위 안/size보다 작고/가장 가까운 값) -> 정렬로 구함
'''


from collections import deque
import sys
input = sys.stdin.readline


def isin(x: int, y: int):
    if -1 < x < N and -1 < y < N:
        return True
    return False


def bfs(x: int, y: int):
    visited = [[False for _ in range(N)]
               for _ in range(N)]    # 방문 체크 겸 dist 저장
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    prey = []   # 먹이만 저장

    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            # print(visited)
            if not isin(nx, ny) or visited[nx][ny]:   # 범위 밖 or 이미 방문
                continue

            # queue 넣을 것
            if arr[nx][ny] <= size:  # 크기가 같아도 이동 가능
                visited[nx][ny] = True
                # print(nx, ny, visited[nx][ny], size)
                queue.append((nx, ny, dist+1))
                # prey 넣을 것
            if 0 < arr[nx][ny] < size:  # 빈 칸(0)이 아니며 본인보다 작은 물고기
                prey.append((nx, ny, dist))

    prey.sort(key=lambda x: (x[2], x[0], x[1]),
              reverse=True)   # 거리 / x / y 순 역정렬
    print(prey)
    return prey.pop() if len(prey) != 0 else (-1, -1, -1)


N = int(input())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
arr = []
start = []

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(N):
        if arr[i][j] == 9:
            start = [i, j]
            arr[i][j] = 0

size = 2
cnt = 0
ans = 0
while True:
    ex, ey, dist = bfs(start[0], start[1])

    if dist == -1:  # 더 이상 먹이가 없는 경우
        break

    ans += dist
    start = [ex, ey]    # 이전 도착지가 다음 출발지

    if cnt == size:
        cnt = 0
        size += 1

print(ans)
