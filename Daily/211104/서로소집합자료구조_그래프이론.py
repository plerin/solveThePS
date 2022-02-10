

'''
1. 부모 테이블 초기화(0)
2. 각 요소의 루트 노드를 찾고 더 큰 부모 노드를 작은 부모 노드로 설정

'''

# 특정 원소 속한 집합 찾기(같은 루트 찾기)


def find_parent(parent, x):
    # 현재 원소와 부모 원소가 다르다면 == 루트가 아니라면 재귀호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기 == 더 작은 부모를 갖는 걸로 갱신


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

# 초기에 부모를 자기 자신 값으로 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 :', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i))

print()

print('부모 테이블 : ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

# 크루스칼 알고리즘
# 무방향 그래프에서 비용이 최솟 값인 최소 신장 트리 만드는 알고리즘


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
ret = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용 순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클아 아니면 == 같은 집합에 포함되어 있지 않으면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ret += cost

print(ret)
