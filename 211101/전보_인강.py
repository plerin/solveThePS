'''
[P]
N개의 도시가 있고 도시 간 통로가 있다. 통로는 방향성이 있다.
C에서 출발하여 메시지를 받는 도시의 개수와 걸리는 시간을 출력

[S]
V와 E로 구성되있는 방향성 그래프 + 출발점이 있고 + 소요 시간 리턴 
    - 유형 : 최단 경로 -> 다익스트라
    - 접근 : 출발지점(C)으로 부터 각 노드간의 최단 거리를 구하고 비용이 INF가 아닌 수(총 도시 개수) + 비용 중 최고 값(총 걸리는 시간)
[L]
1. 입력 받기
    - N, M, C : 모두 INT형 _ 도시 개수 / 통로 개수 / 출발 도시
    - X(int) : 출발 도시 // Y(int) : 도착 도시 // Z(int) : 이동 비용
2. 다익스트라 준비물
    - 라이브러리 추가 : heapq , sys(입력)
    - 전역 변수 : MAX _ int(1e9) // input _ sys.stdin.readline
    - 비용 리스트 : distance(list) _ INF로 N+1개만큼 갱신
3. 다익스트라 함수 선언
    - PARAM : START(tuple) _ (비용,도시)
    - LOGIC
        1) heapq에 출발 도시 담기
        2) while queue -> heapq.heappop() -> dist 값과 distance 값 비교 -> cost(dist+i[1])과 distance 비교
    - RETURN : TRUE
4. 결과 출력
'''

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline


def dijkstra(start):
    queue = []
    heapq.heappush(queue, start)
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra((0, C))

cnt = 0
during_time = 0
for d in distance:
    if d != INF:
        cnt += 1
        during_time = max(during_time, d)

print(cnt-1, during_time)
