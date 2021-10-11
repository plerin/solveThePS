'''
goal : 롤에서 분기점이 N개이고 각 간선이 M개 인 경우 시야가 확보되지 않는 곳을 통해 N까지 가는 최단 경로 구하라
    1) a0 : 0, an-1 : 1
    2) 분기점 간 비용은 양방향성
    3) an : 1인 지역을 제외(an-1은 포함)
0. 라이브러리 추가 : sys(입력), heapq
1. 입력 받기
    1) N,M : 노드와 간선 수
    2) vision : 0(사용가능), 1(사용불가), 단 an-1(목적지)은 사용가능
    3) from,to,cost 
2. 로직
    1) 변수 : graph(인접 노드 비용 입력), distance(방문체크_ INF로 초기화)
    2) graph 입력할 때 vision이 1인 노드(from,to)는 제외하고 입력
    3) 다익스트라 알고리즘 로직 수행 : heapq 활용
3. 결과 반환
'''
# 0
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def shortestPath(s):
    q = [(0, s)]
    distance[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            cc = cost + i[1]
            if cc < distance[i[0]]:
                distance[i[0]] = cc
                heapq.heappush(q, (cc, i[0]))


# 1
N, M = map(int, input().split())
graph = [[] * N for _ in range(N)]
distance = [INF] * (N)

vision = list(map(int, input().split()))
vision[-1] = 0
# limit = []
# for i, v in enumerate(vision):
#     if v == 1 and i != N-1:
#         limit.append(i)

for _ in range(M):
    fr, to, cost = map(int, input().split())
    if vision[fr] == 1 or vision[to] == 1:
        continue
    graph[fr].append((to, cost))
    graph[to].append((fr, cost))


shortestPath(0)

if distance[N-1] == INF:
    print(-1)
else:
    print(distance[N-1])
