'''
>> P
N*M 행렬에서 벽에 대한 질문의 답을 구하여 맵의 형태로 출력
    - 0은 빈 칸 // 1 = 벽을 의미
    - 이동할 수 있는 칸은 '상하좌우'로 고정
    - 질문
        1) 벽을 부수고 이동할 수 있는 곳으로 변경 
        2) 그 위치에서 이동할 수 있는 칸을 구한다
    - 결과를 10으로 나눈 나머지로 출력
>> S
connected-component 유형으로 접근해보자

1. 벽의 좌표를 리스트에 담아 놓는다. or 모든 좌표를 탐색하며(n*m) 벽인 경우(1)에 bfs() 호출
    - 후자 방법으로 모든 좌표를 탐색하며 해당 값이 벽인경우([x][y] == 1) 빈칸을 모두 구하고 10으로 나눈 나머지으로 값 변경
    - for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = solve(i, j)
    --> 이 방법으로 하면 아무리해도 시간초과가 나옴 모든 좌표마다 visited를 False로 갱신하기 때문

2. 플러드 필 알고리즘
    1) 인접해 있는 0을 묶어서 그룹 인덱스를 붙임
        - 모든 보드를 돌면서 0인 경우 visited를 체크하며 보드그룹 인덱스 갱신 & 0개수 반환
            -> visited(list), zero(list)
        - zero[nx][ny] = group

    2) 해당 그룹에 0이 총 몇개가 포함되어있는지 저장하는 딕셔너리 생성
        - 딕셔너리에 그룹 인덱스에 대한 0 개수 저장 
            -> info = {} & info[index] = cnt

    3) 보드를 볼면서 1을 만나면 상하좌우 그룹의 0 개수를 전부 더해 출력
        - candidate = [] & for dx, dy in move & if not zero[nx][ny] -> candidate.append(group) -> cnt += info[group] 
'''

from collections import deque
import sys

input = sys.stdin.readline


def isin(x: int, y: int):
    if -1 < x < N and -1 < y < M:
        return True
    return False


def bfs(x: int, y: int):
    global visited, zero

    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        zero[x][y] = group

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if not isin(nx, ny):
                continue

            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1

                queue.append((nx, ny))

    return cnt


def move_check(x: int, y: int):

    adjacent_grp = set()    # 인접 그룹(상하좌우) 중복 제거
    cnt = 1
    for dx, dy in move:
        nx, ny = x + dx, y + dy

        if not isin(nx, ny):
            continue

        if not zero[nx][ny]:   # (nx, ny)가 벽이면
            continue

        adjacent_grp.add(zero[nx][ny])

    for grp in adjacent_grp:
        cnt += info[grp]

    return cnt % 10  # 결과 값 나머지 10


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]  # 방문 여부 확인
zero = [[0] * M for _ in range(N)]  # 빈 칸(0)을 그룹 묶어줌
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 움직임 범위(상하좌우)

group = 1   # 그룹 1부터 시작
info = {}   # 그룹 별 0 개수 담는 dictionary
for x in range(N):
    for y in range(M):
        if board[x][y] == 0 and not visited[x][y]:  # 빈 칸이면서 방문 안했으면
            cnt = bfs(x, y)
            info[group] = cnt   # group = cnt // 그룹 별 0개수
            group += 1

ans = [[0 for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            ans[x][y] = move_check(x, y)    # 상하좌우 0개수(그룹을 통한) 갱신

for row in ans:
    print(*row, sep='')
