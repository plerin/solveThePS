'''
>> P
N에 있는 수빈이가 K에 있는 동생에게 가는데 걸리는 최소 시간 구하라
    - 이동 방법 +1 / -1 / *2
    - 경로까지 구해야함 -> 경로를 그대로 저장하면 시간 초과, MAX(10만)까지 메모리 생성하면 메모리 초과
>> S
경로를 구하는데 있어서 메모리와 시간을 최소화하는 방벙을 구하기
    - dist로 거리를 저장하고 move(list)로 이전 부모노드를 구해
    - 부모 노드로 넘어가며 경로를 알 수 있다.(거꾸로 출력)

bfs(now: int)
    - logic
        1) deque에 수빈이 현재 위치 담고 방향벡터(dx)로 이동하며 탐색
        2) nx(다음 이동좌표)가 범위 안에 속하고 dist가 0일경우 거리 갱신 & 다음 노드에 현재 노드를 저장(부모노드)
        3) nx가 K인경우 move[nx] dist만큼 반복하며 list를 만들고 거꾸로([::-1]) 출력
'''

from collections import deque
import sys

MAX = 100001


def bfs(now: int):
    global dist, move

    queue = deque([now])
    dist[now] = 1

    while queue:
        x = queue.popleft()

        if x == K:
            return
        for i in range(3):
            nx = eval(str(x)+dx[i])

            if 0 <= nx < MAX and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                move[nx] = x
                queue.append(nx)


N, K = map(int, input().split())
dx = ['+1', '-1', '*2']
dist = [0] * MAX
move = [0] * MAX

bfs(N)

route = []
tmp = K

for _ in range(dist[K]):
    route.append(tmp)
    tmp = move[tmp]

print(dist[K]-1, ' '.join(map(str, route[::-1])), sep="\n")
