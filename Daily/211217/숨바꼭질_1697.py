'''
>> P
수빈이가 N에 있고 동생이 K에 있을 때 수빈이가 이동하여 동생을 찾는 가장 빠른 시간 구하라
    - N,K의 범위는 0~10만
    - 이동 가능 : x+1 / x-1 / x*2
>> S
1. 동적계획법
    - ai = i로 이동하는데 걸리는 최소 시간
    - ai = min(ai+1, ai-1, ai*2) + 1
2. BFS
    - 방향벡터로 이동하다 동생찾으면 리턴
    - *2위치 이동을 어떻게 표현할지? -> '+1', '-1', '*2'를 저장하고 EVAL로 계산!
        - direct = ['+1','-1','*2'] and eval(str(x),direct[i])
'''
from collections import deque
import sys

MAX = 100001


def find_younger(start: int):
    global dist
    if N == K:
        return 0

    queue = deque([start])
    dist[start] = 0

    while queue:
        now = queue.popleft()

        for i in range(len(dx)):
            nx = eval(str(now)+dx[i])
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[now] + 1
                queue.append(nx)
                if nx == K:
                    return


N, K = map(int, input().split())
dx = ['+1', '-1', '*2']
dist = [-1] * MAX
find_younger(N)

print(dist[K])
