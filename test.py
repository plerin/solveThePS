# def recursive(i):
#     if i == 100:
#         return

#     print('{} 번째 재귀함수에서 {} 번째 재귀함수 요청합니다.'.format(i, i+1))
#     recursive(i+1)
#     print('{} 번째 재귀함수를 종료합니다.'.format(i))
#     pass


# recursive(1)


# dfs

# def dfs(graph, node, visit):
#     visit[node] = True
#     print(node, end=' ')
#     for i in graph[node]:
#         if visit[i] == False:
#             dfs(graph, i, visit)


# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visit = [False for _ in range(9)]

# dfs(graph, 1, visit)

from collections import deque
# bfs


def bfs(graph, start, visited):
    d = deque([start])
    visited[start] = True

    while d:
        v = d.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                d.append(i)
                visited[i] = True


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

visited = [False for _ in range(9)]

bfs(graph, 1, visited)
