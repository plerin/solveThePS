'''
>> P
1개의 이모티콘을 S개 만드는데 걸리는 최소 시간을 구하라
    - 1. 모두 복사 / 2. 모두 붙어넣기 / 3. 하나 빼기
>> S
1. 화면 이모티콘과 클립보드 이모티콘의 연관관계를 리스트로 표현
    - dist[s][c] => 화면(s) 이모티콘별 클립보드(c) 이모티콘 개수에 따른 시간 저장
2. 모든 연산을 각자 표현
    - 1번 : dist[s][s] == -1
    - 2번 : dist[s+c][c] == -1 + s+c <= N  
    - 3번 : dist[s-1][c] == -1 + s-1 >= 0
    - 모든 연산(1/2/3)은 가중치가 1 => [s][c] + 1
'''

from collections import deque


def bfs(screen: int, clip: int):
    global dist

    queue = deque([(screen, clip)])
    dist[screen][clip] = 0

    while queue:
        s, c = queue.popleft()

        if s == N:
            return dist[s][c]
        # 1번 연산 : 화면에 있는 모든 이모티콘 복사
        if dist[s][s] == -1:
            dist[s][s] = dist[s][c] + 1
            queue.append((s, s))
        # 2번 연산 : 클립보드에 있는 이모티콘을 붙여넣기
        if s+c <= N and dist[s+c][c] == -1:
            dist[s+c][c] = dist[s][c] + 1
            queue.append((s+c, c))
        # 3번 연산 : 화면에 있는 모든 이모티콘 중 1개 삭제
        if s-1 >= 0 and dist[s-1][c] == -1:
            dist[s-1][c] = dist[s][c] + 1
            queue.append((s-1, c))

    # return min([time for time in dist[N] if time != -1])


N = int(input())
dist = [[-1] * (N+1) for _ in range(N+1)]  # [현재 이모티콘 개수, 클립보드 이모티콘 개수]

ans = bfs(1, 0)

print(ans)
