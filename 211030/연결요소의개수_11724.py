'''
[P]
방향 없는 그래프가 주어졌을 때 연결 요소 구하라

[S]
문제만 봐도 그래프 탐색 _ 노드 간 비용이 같아
    - 유형 : 그래프 탐색 (DFS/BFS) 괘씸해서 2가지 방법으로 모두 풀이한다
[L]
1. 입력 받기
    - N(int) : 노드 수 // M(int) : 간선 수
2. 그래프 탐색 준비물
    - 라이브러리 : from collections import deque(bfs)
    - 그래프 : graph(list) _ 입력 간선으로 풀이
    - 방문처리 : visited(list) _ 노드 수(n)만큼 False로 초기화 _ 방문 시 True
3. 함수 호출(DFS)
    - PARAM : v(int) 노드
    - logic
        1) 방문처리 _ visited[v] = True
        2) 인접 노드 방문 
        3) 방문 안한 지점(False) 재귀 호출
    - True
3. 함수 호출(BFS)
    - PARAM : v(int) _ 노드
    - logic
        1) queue(deque)에 v 담기
        2) while queue
        3) 방문 처리
        4) 인접 노드 방문하며 방문 안한 노드 queue에 담기
'''
from collections import deque
import sys

input = sys.stdin.readline


# def bfs(v):
#     queue = deque([v])

#     while queue:
#         v = queue.popleft()

#         visited[v] = True

#         for i in graph[v]:
#             if visited[i] == False:
#                 queue.append(i)

def dfs(v):
    if visited[v] == True:
        return False

    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

    return True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

if M == 0:
    print(N)
    exit()

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(v)

ret = 0

for i in range(1, N+1):
    if dfs(i) == True:
        ret += 1

print(ret)
