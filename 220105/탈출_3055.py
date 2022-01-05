'''
>> P
R*C 행렬이 있고 S에서 D로 이동할 때 거리는 최소시간을 구하라
    - 이동하는 객체 S와 차오르는 물(*)은 모두 상하좌우로 이동
    - X은 이동할수도 물이 차오를 수도 없다
    - S는 물이 찰 예정인 칸으로 이동할 수 없음
    - D로 도착하지 못하는 경우 'KAKTUS' 출력
>> S
2차원 배열 + 이동 비용 동일 + 최소 시간 == BFS

물의 차오름을 어떻게 표현할 것인지?
    - 바로 생각나는건 while queue -> len(queue) 반복 -> len(water) 반복을 계속 진행
    - S를 반복할 땐 [nx][ny] 주변으로(상하좌우)로 '*'이 없는 경우만 queue에 담기
        & (x, y) == (D좌표) RETURN


다시 짜보자 
global visited를 만들고 고슴도치 이동/ 물이 차오름을 visited[x][y] False -> True로 표시
while queue:
    x, y = queue.pop()를 해도
    # visited[x][y]: continue
    for dx, dy in move:
        nx, ny =...
        if not isin(nx,ny): continue
    -> queue에 고슴도치와 물을 모두 담고 고슴도치면 visited 키워가면서 갱신하면서 진행, 물이면 그냥 1로 채워가며 진행

DOCHI = 1
WATER = 0
1. queue에 고슴도치 / 물을 모두 담음
    - queue = deque([x, y, type]) # type = WATER/DOCHI
    qeueue.append(s좌표)
    queue.append(*좌표)
2. visited = [0] 으로 초기화
3. queue.popleft() 값을 이동할 때마다 visited 갱신
    - if type == DOCHI -> visited[nx][ny] = visited[x][y] + 1
    - if type == WATER -> visited[nx][ny] = 1
queue에 ㅁ

'''

from collections import deque


def isin(x: int, y: int):
    if -1 < x < R and -1 < y < C:
        return True
    return False


def check(x: int, y: int):
    global move
    for dx, dy in move:
        nx, ny = x + dx, y + dy

        if not isin(nx, ny):
            continue
        if forest[nx][ny] == '*':
            return False

    return True


def escape_flood():
    global queue, forest
    # dist = [[False] * C for _ in range(R)]

    while queue:
        x, y, dist, type = queue.popleft()

        # if type == DOCHI and forest[x][y] == '*':
        #     continue

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if not isin(nx, ny) or forest[nx][ny] == 'X':
                continue

            if type == DOCHI:
                print(x, y, nx, ny)
                if forest[nx][ny] == '.' and check(nx, ny):
                    queue.append((nx, ny, dist+1, type))
                elif forest[nx][ny] == 'D':
                    return dist+1
            else:
                if forest[nx][ny] != 'D' and forest[nx][ny] != '*':
                    # print(x, y, nx, ny)
                    forest[nx][ny] = '*'
                    queue.append((nx, ny, dist, type))
    print(forest)
    return 'KAKTUS'


R, C = map(int, input().split())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
forest = []
queue = deque([])

DOCHI = 1
WATER = 0

for i in range(R):
    row = list(input())
    forest.append(row)
    for j in range(C):
        if forest[i][j] == 'S':
            queue.append((i, j, 0, DOCHI))
        elif forest[i][j] == '*':
            queue.append((i, j, 0, WATER))

ans = escape_flood()

print(ans)
