'''
>> P
N*M 지도에서 벽을 1개까지만 부수고 이동할 때 최단경로를 구하라
    - 0 : 이동 가능 // 1 : 벽
    - (1,1) -> (N, M)
    - 상하좌우 이동 가능 
    - 시작 / 끝나는 칸도 카운트 함
2차원 배열에서 최단 경로 구하기
    -> BFS
>> 전략
3차원 배열로 풀어야 하는 문제 
    - [x][y]가 2차원이고 해당 2차원에서 벽을 부술 수 있으면 [1] 없으면 [0] 
    -> 총 [x][y][breakwall] 으로 3차원 으로 풀어야함


'''

from collections import deque


def solve(sx: int, sy: int):
    # dist = [[0] * M for _ in range(N)]    # 거리 저장용 리스트
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         if arr[i][j] == 1:
    #             dist[i][j] = -1
    # dist[sx][sy] = 1
    visit[sx][sy][1] = 1    # [][][1] = 벽을 부술 수 있따. 1회
    queue = deque([(sx, sy, 1)])

    while queue:
        x, y, cnt = queue.popleft()

        if x == N-1 and y == M-1:
            return visit[x][y][cnt]

        for (dx, dy) in move:
            nx = x + dx
            ny = y + dy

            # 범위 내에 있어야 함
            if 0 <= nx < N and 0 <= ny < M:

                # arr[x][y] 가 0이고 dist[x][y]가 1이면 queue에 추가 하고 dist갱신
                if arr[nx][ny] == 0 and visit[nx][ny][cnt] == 0:
                    visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
                # arr[x][y] 가 1이고 dist[x][y]가 0이지만 cnt가 1이이면 dist 갱신
                elif arr[nx][ny] == 1 and cnt == 1:
                    visit[nx][ny][0] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, 0))
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# visit = [[[0] * 2 for i in range(M)] for _ in range(N)]
# print(visit)
ans = solve(0, 0)

print(ans)
