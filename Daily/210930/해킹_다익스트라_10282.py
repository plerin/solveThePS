import sys
import heapq

INF = sys.maxsize


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for _ in range(int(sys.stdin.readline())):
    n, m, start = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m):
        to, fr, cost = map(int, sys.stdin.readline().split())
        graph[fr].append((to, cost))

    ret = dijkstra(start)

    distance = list(filter(lambda x: x != INF, distance))
    print(len(distance), max(distance))
