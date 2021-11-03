'''
[P]
N*N 동굴에서 빠져가나는데 잃는 최소 금액
    - 출발 : [0][0] // 도착 [N-1][N-1]
    - 이동 : 상하좌우 1칸
[S]
2차원 배열에서 출발점에서 도착점까지 이동하며 소모하는 최소 비용
    -> 다익스트라 알고리즘
    - 접근 : 방향벡터 사용하며 distance를 INF로 초기화 & HEAPQ 이용
[L]
1. 키워드 : 입력 값이 0이 들어올 때까지 반복 && 함수 호출하면 반환 값으로 최소 비용 리턴
2. 입력 받기
    - N(INT) : 동굴 N*N _ 만약 0이면 프로그램 종료
    - GRAPH(LIST) : 2차원 배열로 받아
3. 다익스트라 준비물
    - 라이브러리 : HEAPQ, SYS(입력)
    - 함수
4. 함수 선언
    - PARAM : START(INT) : 출발지점
    - LOGIC
        1) DISTANCE(LIST) INF로 초기화
        2) HEAPQ에 QUEUE(START) 담고 반복
        3) 다익스트라 갱신
    - RETURN : 목적지 비용
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def solve(start):
    global n
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    queue = []
    sx, sy = start[0], start[1]
    heapq.heappush(queue, (graph[sx][sy], sx, sy))
    # distance[start[0]][start[1]] = graph[start[0]][start[1]]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist:
            continue

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist+graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                queue.append((cost, nx, ny))
    print(distance)
    return distance[n-1][n-1]


cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    ret = solve([0, 0])

    print(f'Problem {cnt}: {ret}')
