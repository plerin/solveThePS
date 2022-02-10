'''
[P]
N개의 지점과 그 사이를 연결하는 M개의 도로가 있을 때 하나의 도로를 막았을 때 지연시킬 수 있는 최대 시간 구하라
    - 출발은 1 // 도착은 N 이다
    - 지연 효과가 없으면 0 // 무한대면 -1 출력
[S]
노드와 간선으로 구선된 그래프에서 1->N 이동하는데 소요되는 최소 시간 과 간선을 하나씩 없애고 지연되는 시간을 모두 구하기
    - 유형 : 최단거리 (다익스트라)
    - 접근 : 모든 간선을 포함해서 1->N 최소 시간을 구하고 간선을 하나씩 제외하고 걸리는 소요시간으로 결과 도출
    - 다익스트라 시간 복잡도 : O(ElogV) 인데 이걸 간선수 만큼 구해야하니 O(E**2logV) ==> 25,000,000 * log1000 가능할까??
[L]
1. 입력 받기
    - N(INT) : 노드 수 // M(INT) : 간선 수
    - A,B,T : 모두 INT _ FROM TO COST
    - graph(list) : 노드 간 도로 비용
2. 다익스트라 준비물
    - 라이브러리 : sys(입력), heapq(우선순위 큐)
    - 비용 : distance(list) _ INF 값으로 초기화
3. 다익스트라 함수
    - PARAM : START
    - LOGIC
        1) START 비용 갱신 : 0으로
        2) while graph -> heapqpop() -> heappop() -> check the dist -> search near node -> update cost & append heapq 
4. 간선 하나씩 제외하며 다익스트라 호출
'''
from collections import deque
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, v = heapq.heappop(queue)

        if distance[v] < dist:
            continue

        for i in graph[v]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                queue.append((cost, i[0]))


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
edges = []

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    edges.append((a, b, t))

dijkstra(1)

min_exit = distance[N]
delay = 0
for i in range(len(edges)):
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    for a, b, t in edges[:i]+edges[i+1:]:
        graph[a].append((b, t))
        graph[b].append((a, t))

    dijkstra(1)
    delay = max(delay, distance[N])

if delay == INF:
    print(-1)
else:
    print(delay-min_exit)
