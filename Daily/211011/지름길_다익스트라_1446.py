'''
goal : d킬로미터 길이의 도속도로 지날 때 지름길을 이용한 운전 거리 최솟 값 출력
    - 지름길은 일방통행이다
    - 고속도로는 역주행할 수 없다
0. 라이브러리 추가 : sys(입력), heapq
1. 입력 받기
    1) N, D : 지름길 개수, 도속도로 길이
    2) F, T, C : 출발위치, 도착위치, 비용
2. 로직 구성
    1) 변수 선언 - graph : 인접 노드 추가 (toNode,cost), distance : INF으로 N+1만큼 초기화
    2) 다익스트라 알고리즘 수행 : 출발지(0)에서 시작하도록 알고리즘 로직 수행
    3) 결과 출력 - distance[150]
'''

# 0
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def dijkstra(s):
    q = [(0, s)]
    distance[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for n in graph[now]:
            print(n)
            cc = cost + n[1]
            if n[0] <= D and cc < distance[n[0]]:
                distance[n[0]] = cc
                heapq.heappush(q, (cc, n[0]))


# 1
N, D = map(int, input().split())
graph = [[] for _ in range(N+3)]
distance = [INF] * (N+3)

min_v, max_v = 0, 0

for _ in range(N):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))
    min_v = min(min_v, fr)
    if to <= D:
        max_v = max(max_v, to)

graph[0].append((min_v, min_v))

dijkstra(min_v)

ret = 0
if min_v != 0:
    ret += min_v
if max_v != D:
    ret += D-max_v

# print(graph)
print(distance)
