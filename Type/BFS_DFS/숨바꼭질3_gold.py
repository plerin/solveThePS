'''
backjoon url -> https://www.acmicpc.net/problem/13549

>> Keyword
BFS, 이동(dx, dy)
상하좌우이 아닌 경우 이 문제의 경우 1차원 좌표를 ['+1', '-1', '*2'] 이동
특히 '*2'는 0초 소요 -> 1초 소요되는 경우와 차별성 주어야 함!
    => 0초 소요를 1초 소요 이동 값보다 먼저 처리!
    

>> P
수빈이는 N, 동생은 K에 있을 때 수빈이가 동생을 찾는 가장 빠른 시간을 구하라
    - 이동 : +1/1초, -1/1초, *2/0초

>> S
단순한 BFS같지만 0초 후 2*X위치로 이동하는 부분이 걸려 어떻게 처리할까?
가장 빠른 시간을 구하려면 이전 값에 소요시간을 더해야함
-1로 초기화를 하고 출발점을 0으로 두고 순간이동지점 = 원래점그대로 가자

접근
1. BFS로 풀이
2. 이동벡터(move)에 '+1', '-1', '*2'를 두고 eval()로 계산
    - if '*' -> [v] = 이전 값 else -> 이전 값 + 1
    - if v == K : return val 
3. 함수 리턴값 출력

'''
from collections import deque

# 문제 범위의 최대 값 선언
MAX = 100001


def solve(now: int) -> int:
    queue = deque([now])
    dist[now] = 0

    while queue:
        now = queue.popleft()

        if now == K:
            return dist[now]

        # 순간이동(x*2)는 0초 소요이기 때문에 1초 소요보다 더 먼저 나와야 함
        if 0 <= now*2 < MAX and dist[now*2] == -1:
            dist[now*2] = dist[now]
            queue.append(now*2)
        if 0 <= now-1 < MAX and dist[now-1] == -1:
            dist[now-1] = dist[now] + 1
            queue.append(now-1)
        if 0 <= now+1 < MAX and dist[now+1] == -1:
            dist[now+1] = dist[now] + 1
            queue.append(now+1)


N, K = map(int, input().split())
# 방문 체크 + 최소 시간을 구해야하므로 0이 아닌 -1로 초기화
dist = [-1] * MAX

print(solve(N))
