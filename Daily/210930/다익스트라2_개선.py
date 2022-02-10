import heapq

# 무한 값, 10억으로 초기화
INF = int(ie9)

# n = 노드, m = 간선
n, m = map(int, input())
# 출발 노드
start = int(input())
# 연결 리스트 형태 index 0은 버리고 1부터 n까지 사용, tuple(to_node,cost)를 담는다.
graph = [[] for _ in range(n+1)]
# 모든 노드 비용은 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(n):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 비용이 pop된 값보다 작으면 스킵
        if distance[now] < dist:
            continue

        for i in graph[now]:
            # 현재 노드 경유 비용
            cost = distance[now]+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
