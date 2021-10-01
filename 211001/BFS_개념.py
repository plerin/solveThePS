'''
0. 라이브러리 선언 _ deque
1. graph, visited를 초기화  _ n+1개
    1) 그래프는 인접 리스트 형태로 초기화
    2) visited는 방문여부 체크를 위해 False로 초기화 
2. bfs 호출 _ 인자 : 출발 노드 
    1) deque를 선언하고 그 안에 출발노드 넣고 방문체크
    2) while deque돌며 인접리스트 중 방문 안한 노드만 추가

'''
from collections import deque
# 2


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        vec = q.popleft()
        print(vec, end=' ')
        for i in graph[vec]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


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

bfs(1)
