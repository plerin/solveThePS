'''
[P]
M개의 집과 N개의 길이 있는 도시에는 양방향으로 길이 있고 그에 대한 비용이 있을 때 절약할 수 있는 최대 액수
    - 도시는 항상 연결 그래프 형태
[S]
주어진 노드와 간선을 이용해서 최소 신장 트리를 만들고 그렇게 절약할 수 있는 최대 금액(원래 금액 - 최소 신장 트리 금액)을 반환
    - 유형 : 최스 신장 트리 == 크루스칼 알고리즘 활용
[L]
1. 서로소 자료구조 함수 생성
2. 크루스칼 알고리즘 구현
3. 결과 출력(최대 금액 - 최소 금액) == 최대 절약 금액
'''

import sys

input = sys.stdin.readline


def find_parent(x):
    global parent
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


M, N = map(int, input().split())
edges = []
parent = [0] * (M+1)

for i in range(1, M+1):
    parent[i] = i

total_cost = 0
saving_cost = 0

for i in range(N):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    # total_cost += cost

map(int, input())

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        saving_cost += cost
    total_cost += cost
# print(saving_cost)
print(total_cost-saving_cost)
