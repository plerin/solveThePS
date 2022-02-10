'''
[P]
케빈 베이컨 규칙에 따라 유저 수(N)와 친구 관계(M)이 주어졌을 때 케빈 베이컨의 수가 가장 작은 사람 구하기
    - 친구 관계는 양방향성
    - 비용 = 1
    - 여러 명일 경우 번호가 가장 작은 사람 출력
[S]
노드와 간선으로 구성된 그래프에서 각 노드마다 그 외 노드까지의 비용의 합을 구해야함 -> 사람 수 * 연산
    - 유형 : 다익스트라 알고리즘 
[L]
KP : 다익스트라 탐색을 N번만큼 하면서 MIN 값 유지 -> 사람은 1부터 검색하니까 현재 값보다 더 작은 경우에만 갱신
1. 입력 받기
    - N(INT) : 노드 // M(INT) : 간선
    - graph(list) : n+1만큼 만든 후 양방향성으로 입력(비용1)
2. 1~N까지 반복하며 다익스트라 함수 호출 -> 최소 값 갱신
2. 다익스트라 함수
    - PARAM : START(INT) : 출발 노드
    - LOGIC :
        0) DISTANCE 초기화 [INF] * (N+1)
        1) HEAPQ에 QUEUE 담고 DISTANCE[START]=0 갱신
        2) 다익스트라 연산 수행
    - RETURN : 출발 노드부터 그 외 모든 노드들이 비용의 합
3. 결과 출력
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    distance = [INF] * (N+1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, v = heapq.heappop(queue)

        if distance[v] < dist:
            continue

        for i in graph[v]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                queue.append((cost, i))
    return sum(distance[1:])


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

ret = []

for i in range(1, N+1):
    heapq.heappush(ret, (dijkstra(i), i))

print(heapq.heappop(ret)[1])
