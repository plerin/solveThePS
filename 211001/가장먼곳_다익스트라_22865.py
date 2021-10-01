'''
0. 라이브러리 입력 _ sys, heapq
1. 입력 받기 
2. 그래프, distance 초기화 
    1) 그래프는 양방향성
    2) distance는 3개 친구 지점마다 달라 _ 만약 같은 노드면 생략
3. 다익스트라 호출
4. distance 3개 돌아다니며 min이 가장 큰 값 반환(zip으로 묶으면?)
'''
# 0
import sys
import heapq

INF = sys.maxsize


def dijkstra(friend, start):
    q = [(0, start)]
    distance[friend][start] = 0

    while q:
        dist, vec = heapq.heappop(q)

        if distance[friend][vec] < dist:
            continue

        for i in graph[vec]:
            cost = dist + i[0]
            if cost < distance[friend][i[1]]:
                distance[friend][i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


n = int(input())
friend = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
distance = [[INF] * (n+1) for _ in range(3)]

for _ in range(int(input())):
    fr, to, cost = map(int, sys.stdin.readline().split())
    graph[fr].append((cost, to))
    graph[to].append((cost, fr))

for i, f in enumerate(friend):
    dijkstra(i, f)

ret = list(map(min, zip(*distance)))
print(ret.index(max(ret[1:])))
