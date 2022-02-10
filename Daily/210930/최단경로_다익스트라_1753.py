
'''
0. SYS 추가해서 INF = 값 설정 및 앞으로는 INPUT() 대신 SYS.STDIN.READLINE()으로 받자..
1. 입력 값 받아 V,E,START 저장
2. GRAPH , DISTANCE 초기화
3. 다익스트라 알고리즘 호출
    1) priority queue 이용해서 출발지로부터 모든 노드에 최단 경로 구하자 
4. 결과 출력 형식대로 표출
'''

import sys
import heapq
from collections import defaultdict


def dijkstra(start):
    q = [(0, start)]

    while q:
        dist, vec = heapq.heappop(q)

        if vec not in distance:
            distance[vec] = dist

            for i in graph[vec]:
                cost = dist + i[1]
                heapq.heappush(q, (cost, i[0]))


V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())

graph = defaultdict(list)
distance = defaultdict(int)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

ret = dijkstra(S)
# print(graph)
# print(distance)
# 5
for i in range(1, V+1):
    if i == S:
        print(0)
    elif distance[i] == 0:
        print('INF')
    else:
        print(distance[i])
