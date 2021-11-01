'''
[P]
N개의 도시가 있고 도시 간 이동하는 M개의 버스가 있다. A -> B 가는데 드는 최소비용과 경로를 출력하라
    - 범위 : N(1~1000) // M(1~100,000)
[S]
1. 노드와 간선으로 이루어진 그래프에서 a->b 가는데 걸리는 최소비용과 경로
2. 범위 1~1000 && 1~100000
    - 유형 : 다익스트라 (노드와 간선의 범위가 커서 O(ElogV)로 접근해야 함)
    - 접근 : 경로를 어떻게 구할까? heapq에 (비용,노드,경로)를 저장하자
[L]
1. 입력 받기
    - n(int) : 도시 수 // m(int) : 버스 수
    - graph(list) : 도시 간 비용
    - origin(int) : 출발 도시 // destination(int) : 목표 도시
2. 다익스트라 준비물
    - 라이브러리 : sys(입력), heapq
    - 변수 : distance(list) _ INF로 n+1만큼 초기화
3. 함수(getCost)
    - param : origin(int) _ 출발 도시
    - logic
        1) heapq에 담고 출발지 distance 갱신(0)
        2) while qeueu
        3) heapqpop() 하며 비용 체크
        4) 인접 도시 돌며 distance 갱신 -> queue에 담을 때 경로도 입력
    - return : none
4. 결과 출력
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def getCost(start):
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    distance[start] = (0, [start])
    while queue:
        dist, v, route = heapq.heappop(queue)

        if distance[v][0] < dist:
            continue

        for i in graph[v]:
            cost = dist + i[1]
            route.append(i[0])
            if cost < distance[i[0]][0]:
                print(route)
                distance[i[0]] = (cost, route)
                queue.append((cost, v, route))
            route.pop()


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [(INF, [])] * (n+1)

for _ in range(m):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

# print(graph)

o, d = map(int, input().split())

getCost(o)
print(distance)
