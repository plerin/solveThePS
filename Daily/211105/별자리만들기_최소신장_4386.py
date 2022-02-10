'''
[P]
2차원 배열 위 별자리를 만들 때 필요한 최소 비용
    - 별(노드)는 X,Y 좌표로 주어진다.
    - 서로 다른 두 별을 일직선으로 이은 형태
    - 모든 별은 서로 직/간접적으로 이어져 있어야 한다 == 연결 리스트 
[S]
최소 신장 트리 만드는 문제
    - 노드가 2차원 배열 위 X,Y 좌표로 주어지고 간선이 없다 -> 노드를 입력 받은 뒤 모든 노드를 잇는 간선을 만들어줘야지
    - 별들 간 거리구하는 연산 함수로 만들기 
        1) 좌표를 인덱스에 매칭 
        2) 좌표간 
[L]
1. 간선 만들기 - 두 별 사이의 거리 
    - 두 별사이의 거리 ==  피타고라스
    - 모든 별에서 2개 선택하는 경우의 수(순열)로 거리를 구하고 그걸 EDGES 에 담아놓기
    - 
'''
from itertools import permutations


def getDistance(a, b):
    x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dist


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


n = int(input())
stars = [0] * (n+1)
parent = [0] * (n+1)
edges = []

for i in range(1, n+1):
    parent[i] = i
    stars[i] = list(map(float, input().split()))

comb = permutations(range(1, n+1), 2)

for a, b in comb:
    dist = getDistance(stars[a], stars[b])
    edges.append((dist, a, b))

edges.sort()
ret = 0

for edge in edges:
    dist, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ret += dist

print('{0:.2f}'.format(ret))
