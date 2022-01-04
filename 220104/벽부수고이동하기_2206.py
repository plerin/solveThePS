'''
>> P
N*M 맵에서 (1,1) -> (N,M) 위치를 이동하는데 걸리는 최소 시간을 구하라
    - 벽을 한개까지 부수고 이동가능
    - 상하좌우 이동 가능
>> S
2차원 배열에서 최단 경로 -> BFS
>> 전략
벽을 부수고 이동하는 경우를 고려해야 함
    -> 각 좌표마다 벽 부술 수 있는 카운트를 추가
    -> 3차원 배열 [x][y][z] -> (x,y)좌표에서 진행한 벽 부순 횟수(z)
'''

from collections import deque


def solve():
    # (x,y)에서 벽 부수기 횟수를 위한 3차원 배열
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    queue = deque([(0, 0, 0)])
    visit[0][0][0] = 1  # 출발점(0,0)에서 0번 벽 부순 값에 1로 초기화

    while queue:
        x, y, cnt = queue.popleft()

        if x == (N-1) and y == (M-1):
            return visit[x][y][cnt]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][cnt]:
                if arr[nx][ny] == 0:
                    visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
                # 이동할 좌표가 벽(1)이고 부수기 횟수가 남았을 때
                elif arr[nx][ny] == 1 and cnt < 1:
                    visit[nx][ny][cnt+1] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt+1))

    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 이동반경 (상/하/좌/우)

print(solve())
