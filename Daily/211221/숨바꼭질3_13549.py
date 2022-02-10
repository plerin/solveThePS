'''
>> P
N에 있는 수빈이가 K에 있는 동생을 찾는데 걸리는 최소 시간을 구하라
    - 수빈, 동생 모두 X좌표 위에 있다(0~10만)
    - 1초 후 : +1 / -1  도는 0초 후 : *2 만큼 이동
>> S
좌표에서 가장 빠른 시간을 구하라
    - BFS
0초 후 2*X 이동
    - 좌표를 이동할 때마다 *2를(<=10만) 구해서 선점해놓기(-1 -> [x]+1)
'''

from collections import deque

MAX = 100001


def bfs(now: int):
    global dist

    q = deque([now])
    dist[now] = 0

    while q:
        x = q.popleft()

        if x == K:
            return dist[x]

        # 순간이동 _ 다른 이동 연산보다 우선순위를 높이기위해 appendleft()사용
        # 생각을 해봤는데 우선순위를 높이지 않으면 +1/-1 연산보다 더 늦게 들어와서 예상한 값이 안 나올 수 있어!
        if x*2 < MAX and dist[2*x] == -1:
            dist[2*x] = dist[x]
            q.appendleft(2*x)

        # 1초 후 이동(앞 / 뒤)
        for i in range(2):
            nx = x + dx[i]

            if 0 <= nx < MAX and dist[nx] == -1:
                q.append(nx)
                dist[nx] = dist[x] + 1


N, K = map(int, input().split())
dist = [-1] * MAX
dx = [1, -1]

ans = bfs(N)

print(ans)
