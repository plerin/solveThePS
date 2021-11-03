'''
[P]
N개의 헛간 M개의 양방향 길이 있는 농장에서 숨바꼭질. 최대한 멀리 숨을 수 있는 헛간은?
    - 멀리 숨는다 == 출발지(1에서) 이동하는 길의 최대 개수
    - 모든 헛간 간 거리의 비용은 1
    - 결과 출력 값은 3개 : 숨는 헛간 // 거리 // 같은 거리 갖는 헛간 개수
[S]
그래프에서 출발 노드에 대한 최대 거리 노드 // 거리 // 같은 거리 갖는 헛간
    - bfs / 다이나믹 프로그래밍
    - 노드가 2만개라 플로이드 워셜은 사용 못함
[L]
BFS 풀이 
    - 인접 노드를 돌며 기존 값 + 1 로 비용 ==> 비용이 같기 때문에 가능
다익스트라 풀이
    - 우선순위 큐로 이용해서 최소 비용 값을 갱신하며 풀이
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def solve(start):
    global N, graph
    distance = [INF] * (N+1)

    queue = []
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

    return distance


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

ret = solve(1)

max_val = max(ret[1:])

print(ret.index(max_val), max_val, ret.count(max_val))
