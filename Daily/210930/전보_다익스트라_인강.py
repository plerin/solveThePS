import heapq
import sys
# 다익스트라 함수
# 방문체크할 때 cnt + 1 (총 개수) , cost 중 max값 지속 저장


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            c = distance[now] + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))


# INF 설정
INF = sys.maxsize

# 입력 받아 초기 환경 셋팅 _ graph, distance 초기화 (INF)
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# GRAPH 입력
for _ in range(m):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

# 다익스트라 호출
dijkstra(start)
ret = list(filter(lambda x: x != INF, distance))
print(len(ret)-1, max(ret))
# 결과 출력 ( 총 개수, 시간)
# print(*ret)
