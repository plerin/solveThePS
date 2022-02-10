'''
>> P
N*M 행렬 위에 (1,1) -> (N,M) 가는 최소 경우를 구하라
    - 상하좌우로 이동 가능
    - K개만큼 벽을 부수고 이동할 수 있다.
    - 불가능 할 경우 -1 출력
>> S
1. 벽 부수는 경우도 배열로 추가하여 3차원 배열을 선언
    - [x][y][z] => (x,y)에서 z번 부수고 간 이동횟수
    - 0~K개까지 부수고 이동할 수 있으니까 [0] 부터 값을 갱신하여 부술 때마다 +1씩 더해줌
'''

from collections import deque
import sys

input = sys.stdin.readline


def solve(x: int, y: int):
    visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]  # 3차원 배열 초기화

    queue = deque([(x, y, 0)])
    visit[x][y][0] = 1  # 출발점 부수기 누적 회수(0) 초기화 -> K개까지 가능

    while queue:
        x, y, cnt = queue.popleft()

        if x == N-1 and y == M-1:
            return visit[x][y][cnt]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny][cnt]:

                if arr[nx][ny] == 0:
                    visit[nx][ny][cnt] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
                elif arr[nx][ny] == 1 and cnt < K:
                    visit[nx][ny][cnt+1] = visit[x][y][cnt] + 1
                    queue.append((nx, ny, cnt+1))


N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(solve(0, 0))
