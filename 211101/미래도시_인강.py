'''
[P]
1~N까지 회사가 있고 회사 간에는 도로가 이용할 수 있어, 1번에서 K번 회사를 방문한 뒤 X번 회사로 가는 최소 시간을 구하라
    - 도로 특징 : 양방향성 // 비용은 모두  1
[S]
회사(노드)와 도로(간선)이며 비용은 모두 1인 양방향성 그래프
    - 특징으로는 1->K->X 로 가야하는데 최소 비용 == 최단 경로
    - K번을 경유하고 N,M의 범위가 100이하
    = 유형 : 플루이드 워셜 -> 점화식을 이용해 O(N**3)의 시간복잡도로 모든 노드에서 다른 노드로의 최단경로 구할 수 있음
[L]
1. 입력 받기
    - N(int) : 회사 수 // M(int) : 도로 수 == 간선
    - graph(list) : 회사 간 간선 , 비용은 모두 1  && 양방향
    - X(int) : 목표 회사 // K(int) : 경유 회사
2. 풀이 방법
    - 입력 값으로 graph를 초기화 한 후에 경유지(k)로의 비용을 갱신하고 결과 출력(graph[1][x])
'''

import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    f, t = map(int, input().split())
    graph[f][t] = 1
    graph[t][f] = 1

X, K = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

ret = graph[1][K]+graph[K][X]
if ret >= INF:
    print(-1)
else:
    print(ret)
