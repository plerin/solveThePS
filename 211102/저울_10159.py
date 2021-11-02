'''
[P]
각 물건에 대해서 다른 물건들 과의 비교 결과가 있을 때 각 물건에 대해 비교 결과를 알 수 없는 물건의 개수를 출력
    - 각 물건에 대해 연결되지 않은 물건 개수를 구하라
[S]
유형 : 
    1. 다익스트라 알고리즘 _ 각 노드를 바탕으로 비용을 inf로 두고 도달하지 못해 inf로 남아있는 경우 리턴
        - 접근 : 각 노드마다 다익스트라 알고리즘의 결과로 주어지는 DISTANCE에서 INF인 결과 값 출력
    2. BFS _ 커넥티드 컴포넌트 유형으로고 가능
[L]

'''
import heapq
import sys

input = sys.stdin.readline
# INF =


def dijkstra(start):
    queue = []
    # distance = [INF] * (N+1)
    visited = [False] * (N+1)
    heapq.heappush(queue, (start))

    while queue:
        v = heapq.heappop(queue)
        visited[v] = True

        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)

    return sum([1 for i in visited if i == False]) - 1


N = int(input())
M = int(input())
compare = []

for _ in range(M):
    f, t = map(int, input().split())
    compare.append((f, t))
    # graph[f].append(t)

for i in range(1, N+1):
    graph = [[] for _ in range(N+1)]
    for a, b in compare:
        if b == i:
            graph[b].append(a)
        graph[a].append(b)
    print(dijkstra(i))
