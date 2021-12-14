'''
>> P
그래프 정점의 집합을 둘로 분할해 집합에 속한 정점끼리 서로 인접하지 않는 경우 = 이분그래프
입력 받은 그래프가 이분 그래프인지 판별하여 출력
    - V, E : 정점 수, 간선 수
>> S
이분 그래프 의미 파악
정점끼리 서로 인정하지 않도록 분할할 수 있으면 이분 그래프
인접한 정점끼리 서로 다른 색으로 ㅣㄹ해서 모든 정점을 두가지 색으로만 칠할 수 있는 그래프
시간복잡도 : 모든 정점을 방문하며 간선을 검사 => O(V+E)

BFS / DFS 풀이모두 있지만 E의 최대 값이 20만이니까 BFS 풀이해보자
    - -1 / 0 / 1 : -1(기본 값), 0(색상1), 1(색상2), 기본 값으로 초기화 후 색상에 반대 값을 칠하며 채워나감
'''
from collections import deque
import sys

input = sys.stdin.readline


def bfs(v: int):
    global vertex

    queue = deque([v])

    while queue:
        v = queue.popleft()
        if vertex[v] == -1:
            vertex[v] = 0

        for i in graph[v]:
            if vertex[i] == -1:
                vertex[i] = 1 if vertex[v] == 0 else 0
                queue.append(i)
            elif vertex[v] == vertex[i]:
                return False

    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    vertex = [-1] * (v+1)
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_graph = True

    for i in range(1, v+1):
        if not bfs(i):
            is_graph = False

    if is_graph:
        print("YES")
    else:
        print("NO")
