
INF = int(ie9)

n, m = map(int, input().split())
start = int(input())
# 노드 별 연결 리스트 형태 (to_node,cost)
graph = [[] for _ in range(n+1)]
# 방문 여부 체크
visited = [False] * (n+1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(n):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

# 방문하지 않은 노드 중 최단 거리 노드 반환


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return i


def dijkstra(start):
    distance[start] = 0  # 출발 노드의 cost는 0
    visited[start] = True  # 출발 노드 방문 처리
    for j in graph[start]:  # 출발 인접 노드 거리 초기화
        distance[j[0]] = j[1]

    for i in range(n-1):    # 출발노드 제외한 노드 반복 == range(n-1)
        now = get_smallest_node()
        visited[now] = True  # 방문 처리
        for j in graph[now]:
            # 현재(now) 노드까지의 cost + 현재 노드에서 인접노드(j[0])가는 cost
            cost = distance[now] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost  # 최소 비용으로 갱신


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
