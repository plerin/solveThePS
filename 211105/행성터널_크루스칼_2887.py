'''
[P]
N개의 행성으로 이루어진 왕국에서 모든 행성을 터널로 연결하는데 필요한 최소 비용
    - 터널 연결 비용 : min(|x-x|,|y-y|,|z-z|)
    - 터널을 n-1개 -> 모든 행성 서로 연결
[S]
간선을 N-1개 만들어서 모든 행성 서로 연결되도록
    - 유형 : 최소 신장 트리 
    - 알고리즘 : 크루스칼
[L]
1. 노드가 좌표로 주어져 있으니 노드를 입력 받고 노드 간 간선 계산하여 EDGES 에 담아 최소 신장 트리 구하기

풀이
    1. 인덱스틀 포함해서 노드를 입력 받아
    2. copy로 x/y/z 기준 정렬한 리스트 생성
    3. copy한 리스트마다 n-1번 반복하며 가장 근접한 노드 간 거리와 인덱스를 edges에 저장
    4. 이후는 크루스칼 알고리즘 로직 수행
'''
# from itertools import permutations
import sys
import copy

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


N = int(input())
planet = []
edges = []
for i in range(N):
    planet.append((i,) + tuple(map(int, input().split())))

planet_x = copy.deepcopy(planet)
planet_y = copy.deepcopy(planet)
planet_z = copy.deepcopy(planet)

planet_x.sort(key=lambda x: x[1])
planet_y.sort(key=lambda x: x[2])
planet_z.sort(key=lambda x: x[3])

for i in range(len(planet_x)-1):
    edge = (abs(planet_x[i+1][1]-planet_x[i][1]),
            planet_x[i+1][0], planet_x[i][0])
    edges.append(edge)

for i in range(len(planet_y)-1):
    edge = (abs(planet_y[i+1][2]-planet_y[i][2]),
            planet_y[i+1][0], planet_y[i][0])
    edges.append(edge)

for i in range(len(planet_z)-1):
    edge = (abs(planet_z[i+1][3]-planet_z[i][3]),
            planet_z[i+1][0], planet_z[i][0])
    edges.append(edge)

edges.sort()

parent = [0] * N

for i in range(N):
    parent[i] = i

ret = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ret += cost

print(ret)
