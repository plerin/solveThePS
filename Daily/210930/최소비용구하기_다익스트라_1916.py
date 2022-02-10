'''
0. 라이브러리 _ sys - 입력받기 . heapq - 우선순위 큐
1. 입력 받기 _ N,M (노드/간선)
2. 그래프 및 거리 리스트 초기화 
    1) 그래프 - 연결 리스트 형식 g[from]=(to,cost) _ N+1개(0은 사용 안해)
    2) 거리 - INF(무한) 으로 N+1개 
3. 다익스트라 호출 _ 인자 : start - 출발 지점 
    1) q 만들고 distance 초기화(0)
    2) while q 돌며 heapq 로 빼고 distance 에 따라 continue
    3) 경유 비용이 distance 값보다 작은 경우 갱신 및 heapq추가
4. distance에서 D 값 출력
'''
import sys
import heapq

INF = sys.maxsize


def dijkstra(origin):
    q = [(0, origin)]
    distance[origin] = 0

    while q:
        dist, vec = heapq.heappop(q)

        if dist > distance[vec]:
            continue

        for i in graph[vec]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n = int(input())
m = int(input())

# 2
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    fr, to, cost = map(int, sys.stdin.readline().split())
    graph[fr].append((to, cost))

o, d = map(int, sys.stdin.readline().split())

# 3
dijkstra(o)

# 4
print(distance[d])
