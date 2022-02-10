'''
>> P
트리가 입력으로 주어질 때 트리의 지름을 구하라
    - 정점은 1~V까지 v개가 있음
>> S
트리의 지름을 구하는 방법은 
    1. 임의의 정점에서 가장 먼 정점을 찾는다. 
    2. 1번에서 찾은 정점에서 가장 먼 정점까지의 거리를 반환한다.
    -> dfs/bfs 방식으로 가장 먼 정점을 찾는 행동을 2번 수행하면 구할 수 있음

'''

from collections import deque
import sys

input = sys.stdin.readline


def cal_diameter(node: int):
    dist = [-1] * (V+1)
    ret = (0, node)

    queue = deque([node])
    dist[node] = 0

    while queue:
        node = queue.popleft()

        if ret[0] < dist[node]:     # 임의 노드(node)부터 현재 노드까지의 거리가 더 크면 갱신
            ret = (dist[node], node)

        for w, n in graph[node]:
            if dist[n] != -1:
                continue
            dist[n] = dist[node] + w
            queue.append(n)

    return ret  # 임의 노드에서 가장 먼 거리와 노드를 반환


V = int(input())  # 정점 개수
graph = [[] for _ in range(V+1)]

for _ in range(V):
    v, *info = map(int, input().split())
    for i in range(0, len(info)-1, 2):  # 마지막 -1 제외, 2칸씩 이동하며 weight, node 인접 노드로 등록
        node, weight = info[i], info[i+1]
        graph[v].append((weight, node))

tmp = cal_diameter(1)
ans = cal_diameter(tmp[1])
print(ans[0])
