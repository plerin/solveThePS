
'''
0. 라이브러리 추가 _ collections-defaultdict, sys, heapq
1. 입력 값 받기
2. GRAPH, PATH 초기화 , PATH에는 (TONODE, PATH/FIRST NODE)
3. 노드 별 다익스트라 호출
    1) 우선순위 큐를 통한 최단 경로 구해
    2) 출발(S)부터 다른 노드의 첫 노드를 리스트 형식으로 반환
4. 반환 값 형식대로 표출
'''

import collections
import sys
import heapq


def dijkstra(start):
    q = [(0, start, start)]
    path = collections.defaultdict(str)

    while q:
        cost, prev, now = heapq.heappop(q)

        if now not in path:
            path[now] = prev

            for i in graph[now]:
                nc = cost+i[1]
                heapq.heappush(q, (nc, now, i[0]))
    # for k in sorted(path):
    #     print(k, path[k])
    return list(map(lambda x: path[x], sorted(path)))


n, m = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)

for _ in range(m):
    f, t, c = map(int, sys.stdin.readline().split())
    graph[f].append((t, c))
    graph[t].append((f, c))

ret = []
for i in range(1, n+1):
    # print(dijkstra(i))
    ret.append(dijkstra(i))

# print()

ret = list(map(list, zip(*ret)))
for i in range(n):
    for j in range(n):
        if i == j:
            print('-', end=' ')
        else:
            print(ret[i][j], end=' ')
    print()

    # print(path)
    # for j in range(len(shortest)):
    #     if i == j:
    #         print('-', end=' ')
    #     else:
    #         print(shortest[j], end=' ')
    #     print()
