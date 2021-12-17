'''
>> P
1~N 번호의 정점이 N개가 있다 트리가 주어졌을 때 올바른 DFS 방문 순서 여부 확인하라
    - 시작은 1번
    - 양방향 그래프
>> S
BFS 스페셜저지 문제랑 유사하게 접근하기
order(list)의 인덱스를 트리 값, 값을 인덱스(=우선순위)로 초기화하고
graph를 order로 정렬한 뒤 정렬된 graph 값으로 DFS를 구하기
'''

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(node: int):
    global visited, ret

    visited[node] = True

    for vec in graph[node]:
        if not visited[vec]:
            ret.append(vec)
            dfs(vec)


N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ret = [1]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

tree = list(map(int, input().split()))
order = [0] * (N+1)

for i in range(len(tree)):
    order[tree[i]] = i

for i in range(len(graph)):
    graph[i].sort(key=lambda x: order[x])

dfs(1)

if ret == tree:
    print(1)
else:
    print(0)
