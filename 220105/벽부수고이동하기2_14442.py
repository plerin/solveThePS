'''
>> P
N*M 행렬 위 (1,1) -> (N,M)을 가려고 할 때 최소 이동 횟수를 구하라
    - 상하좌우로 이동 가능
    - Ko개 벽을 부수고 이동할 수 있음
    - 출발/도착점 칸도 포함하여 카운트
>> S
2차원 행렬 위 최단경로 + 이동비용이 모두 같을 때 == BFS

1. 좌표마다 벽을 부술 수 있는 횟수가 있어야해 -> 2차원 + 1차원 == 3차원
    - [x][y][z] = (x,y)에서 z번 벽을 부순 횟수
    - 다음 좌표가 벽(1)이면서 cnt < K 라면 [nx][ny][cnt+1] = [x][y][cnt] + 1
2. N,M의 범위가 크다보니 최대한 시간 효율적으로 코드 구성해야 함
    - pypy 제출 고려
    - input = sys.stdin.readline 사용
'''

from collections import deque
import sys

input = sys.stdin.readline


def isin(x: int, y: int):
    if -1 < x < N and -1 < y < M:
        return True
    return False


def solve():
    visited = [[[False for _ in range(K+1)]
                for _ in range(M)] for _ in range(N)]

    queue = deque([(0, 0, 0, 1)])   # (출발x, 출발y, 벽 부술수 있는 횟수, 거리)
    visited[0][0][0] = True  # (x, y, cnt)

    while queue:
        x, y, cnt, dist = queue.popleft()

        if x == (N-1) and y == (M-1):   # 조건 만족
            return dist

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if not isin(nx, ny):
                continue    # 범위(N,M) 벗어나면

            if visited[nx][ny][cnt]:    # 이미 방문한 경우
                continue

            if arr[nx][ny] == 0:
                visited[nx][ny][cnt] = True
                queue.append((nx, ny, cnt, dist+1))
            elif cnt < K and not visited[nx][ny][cnt+1]:    # 다음 좌표가 벽이면서 방문한 경우
                visited[nx][ny][cnt+1] = True
                queue.append((nx, ny, cnt+1, dist+1))

    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우 이동

ans = solve()

print(ans)
