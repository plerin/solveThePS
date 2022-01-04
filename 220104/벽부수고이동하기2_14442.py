'''
>> P
N*M 지도 위 (1,1) -> (N,M)으로 이동하는 데 걸리는 최소 시간을 구하라
    - 상하좌우로만 이동 가능
    - K개 만큼 벽을 부수고 이동가능
    - 출발점/도착점을 모두 카운트 함

-> 2차원 배열 위 최단 경로 == BFS

>> S
1. 벽을 K개까지 부수고 이동 가능
    -> 3차원 배열로 각 좌표마다 K+1개 크기를 만들어놓고 풀이
    -> 벽을 부술 때마다 cnt+1, 만나는 좌표가 벽이고 cnt가 K보다 작다면 cnt +1 하고 지나가 
'''

from collections import deque


def solve(start: tuple):
    visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    queue = deque([(start[0], start[1], K)])
    # visit[start[0]][start[1]][0] = 1
    visit[start[0]][start[1]][K] = 1
    while queue:
        x, y, cnt = queue.popleft()
        # print(visit)
        if x == (N-1) and y == (M-1):
            return visit[x][y][cnt]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][cnt]:
                if arr[nx][ny] == 0:
                    visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
                # elif arr[nx][ny] == 1 and cnt < K:
                    # visit[nx][ny][cnt+1] = visit[x][y][cnt] + 1
                    # queue.append((nx, ny, cnt+1))
                elif arr[nx][ny] == 1 and cnt > 0:
                    visit[nx][ny][cnt-1] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt-1))


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ans = solve((0, 0))

print(ans)
