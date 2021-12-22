'''
>> P
주어진 트리의 지름을 구하라
    - 트리의 지름 = 모든 경로들 사이 중 가장 긴 것의 길이
    - 입력 값은 작은 값 -> 큰 값 순서(부모 자식 가중치)
    - 루트 노드는 1
>> S
1. 임의 정점에서 가장 먼 노드를 찾는다
2. 1번에서 찾은 노드에서 가장 먼 노드를 찾고 그 길이를 구하면 지름
이 때 필요한 가장 먼 노드를 찾는 방법
    - 노드와 가중치를 저장해놓고 갱신해 어떤 자료형 사용하지? -> tuple (가중치, 노드)
    - 노드를 입력받고 해당 노드에서 가장 먼 노드를 찾는 dfs함수 만들고 이걸 2번 불러!

'''
from collections import deque


def dfs(node: int):
    global dist

    for w, n in graph[node]:
        if dist[n] != -1:
            continue
        dist[n] = dist[node] + w
        dfs(n)


# dist = [-1] * (N+1)
# ret = (0, node)

# print(dist)

def cal_diameter(node: int):
    dist = [-1] * (N+1)

    stack = [node]
    dist[node] = 0
    ret = (0, node)

    while stack:
        node = stack.pop()

        if dist[node] > ret[0]:
            ret = (dist[node], node)

        for w, n in graph[node]:
            if dist[n] != -1:
                continue
            dist[n] = dist[node] + w
            stack.append(n)

    return ret

# def cal_diameter(node: int):
#     dist = [-1] * (N+1)

#     queue = deque([node])
#     dist[node] = 0
#     ret = (0, node)

#     while queue:
#         node = queue.popleft()

#         if dist[node] > ret[0]:
#             ret = (dist[node], node)

#         for w, n in graph[node]:
#             if dist[n] != -1:
#                 continue
#             dist[n] = dist[node] + w
#             queue.append(n)

#     return ret


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((weight, child))
    graph[child].append((weight, parent))

# farthest_node = cal_diameter(1)
# ans = cal_diameter(farthest_node[1])
# print(ans[0])

dist = [-1] * (N+1)
dist[1] = 0
dfs(1)
far = dist.index(max(dist))
dist = [-1] * (N+1)
dist[far] = 0
dfs(far)
print(dist)
