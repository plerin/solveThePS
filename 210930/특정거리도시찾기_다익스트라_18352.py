from collections import defaultdict
import heapq
import sys


def dijkstra(start):
    q = []
    ans = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if now not in distance:
            distance[now] = dist
            if dist == k:
                ans.append(now)

            for i in graph[now]:
                cost = dist + i[1]
                heapq.heappush(q, (cost, i[0]))

    return sorted(ans)


n, m, k, x = map(int, input().split())

graph = defaultdict(list)
distance = defaultdict(int)

for _ in range(m):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1].append((c2, 1))

ret = dijkstra(x)

if len(ret) == 0:
    print(-1)
else:
    print(*ret, sep='\n')


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


n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1].append((c2, 1))

dijkstra(x)

# ret = sorted(list(filter(lambda x: x[1] == k, enumerate(distance))))
ret = sorted(list(map(lambda x: x[0], filter(
    lambda x: x[1] == k, enumerate(distance)))))

if len(ret) == 0:
    print(-1)
else:
    print(*ret, sep='\n')
