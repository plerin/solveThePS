'''
Breadth-First-Search, 너비 우선 탐색

가까운 노드부터 우선적으로 탐색하는 알고리즘
Queue를 이용

++
최단경로 알고리즘으로도 사용 - 간선의 비용이 동일한 경우!
'''

from collections import deque


def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        n = queue.popleft()

        print(n, end=' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
