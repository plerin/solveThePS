'''
1. graph, visited 초기화
    1) graph는 양방향성 그래프로 인접노드를 추가 _ n+1
    2) visited는 방문여부 확인 False로 초기화 _ n+1(index 0은 안쓸것)
2. dfs 호출 _ 그래프, 출발노드, 방문리스트
    1) 방문 체크
    2) 인접노드 중 방문하지 않은 노드를 재귀 호출
'''


def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


# 1
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

dfs(1)
