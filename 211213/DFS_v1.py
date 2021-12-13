def dfs(graph, v, visited):
    # 방문처리
    visited[v] = True
    # 출력
    print(v, end=' ')
    for i in graph[v]:
        # 현재 노드(v)와 인접한 노드 중 방문하지 않은 노드에 대해서 재귀호출
        if not visited[i]:
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)
