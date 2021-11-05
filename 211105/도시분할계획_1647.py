'''
[P]
N개 집과 M개 길로 이루어진 마을의 유지비를 줄이력 ㅗ한다.
    - 두 마을 사이의 길은 없앨 수 있다.
    - 두 집 사이에 경로가 항상 존재하면서 최소화 할 수 있다.
[S]
N개의 노드와 M개의 간선이 있을 때 간선의 비용이 최소화 될 수 있도록 하자
    -> 최소 신장 트리
    -> 크루스 칼 알고리즘
[L]
두 개의 분리된 마을에서 최소 유지비용-> 최소 신장 트리로 만든 후 가장 비용이 높은 걸 끊어버리기
'''
import sys

input = sys.stdin.readline


def find_parent(x):
    global parent
    # 노드 x의 루트가 x가 아니면 == x의 루트 노드가 입력 값이 아니라면
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
edges = []
parent = [0] * (N+1)
ret = []

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ret.append(cost)

print(sum(ret[:-1]))
