'''
1개 입력 -> 3가지 연산으로 S개 만들기
모든 연산을 1초 걸릴 때 시간 최솟값을 구하라
>> P
1개를 S개로 만드는 최소 시간을 구하라
    - 모든 연산은 1초가 걸림
>> S
모든 연산이 1초가 걸리고 최소 시간을 구하라 
    -> 같은 가중치에 최솟값은 BFS풀이
화면 이모티콘과 클립보드 이모티콘 관계로 풀이하기
    -> [s][c] => 화면 이모티콘(s) // 클립보드(c)
>> F
def bfs(s: int, c: int)
    - param : 화면 이모티콘 수, 클립보드 이모티콘 수
    - vari : dist(list) _ 이중 배열을 MAX(1001) 크기로 -1 초기화
    - logic
        1) s와 c를 deque에 담고 dist[s][c] = 0
        2) deque를 반복하며 3가지 연산을 풀이해 모두 가중치 = 1
            - 0~MAX 범위 안에 있고 '-1'인 경우만 
'''

from collections import deque

MAX = 1001


def bfs(s: int, c: int):
    global dist

    queue = deque([(s, c)])
    dist[s][c] = 0

    while queue:
        s, c = queue.popleft()

        if s == S:
            return dist[s][c]

        if dist[s][s] == -1:
            dist[s][s] = dist[s][c] + 1
            queue.append((s, s))
        if s+c < MAX and dist[s+c][c] == -1:
            dist[s+c][c] = dist[s][c] + 1
            queue.append((s+c, c))
        if s-1 >= 0 and dist[s-1][c] == -1:
            dist[s-1][c] = dist[s][c] + 1
            queue.append((s-1, c))


S = int(input())
dist = [[-1] * MAX for _ in range(MAX)]

ans = bfs(1, 0)

print(ans)
