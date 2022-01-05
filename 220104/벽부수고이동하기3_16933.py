'''
>> P
점점 더 재밌어지는 문제
낮과 밤이 있고 한번 이동할 때마다(머물러 있는것도 포함) 낮과 밤이 바뀐다.
    - 단 벽은 낮에만 부술 수 있다.

>> S
낮과 밤 그리고 벽 부수는 걸 어떻게 연관 지을까?
전역변수로 night = False 만들고 이동할 때마다(현재 있는 모든 값을 꺼낼 때, 새롭게 추가되는 값 제외)

멈춘 경우 추가 어떻게?
    - 기존 visited를 통해 방문여부 체크했는데 가만히 있는경우는 어떻게 처리?
    -> visited 그대로 사용하되 nx,ny == x,y 라면 queue에 담아준다
'''
from collections import deque
import sys

input = sys.stdin.readline

DAY = 0
NIGHT = 1


def isin(x: int, y: int):   # 해당 좌표가 범위 안에 해당하면 True <-> False
    if -1 < x < N and -1 < y < M:
        return True
    return False


def solve(x: int, y: int):
    visited = [[[False for _ in range(K+1)]
                for _ in range(M)] for _ in range(N)]
    q = deque([(x, y, 0, 1, DAY)])  # [x, y, 벽 부순 횟수, 거리, 밤/낮]
    visited[x][y][0] = True
    while q:
        x, y, cnt, dist, time = q.popleft()

        if x == (N-1) and y == (M-1):
            return dist

        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            next_time = DAY if time == NIGHT else NIGHT  # 밤/낮 toggle

            if not isin(nx, ny):
                continue

            if arr[nx][ny] == 0:
                if not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = True
                    q.append((nx, ny, cnt, dist+1, next_time))
            elif cnt < K:
                if not visited[nx][ny][cnt+1]:
                    if time == DAY:
                        visited[nx][ny][cnt+1] = True
                        q.append((nx, ny, cnt+1, dist+1, next_time))
                    else:
                        q.append((x, y, cnt, dist+1, next_time))
    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우 이동

ans = solve(0, 0)   # 출발점 입력

print(ans)
