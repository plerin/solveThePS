'''
[P]
모든 컴퓨터를 연결하는 네트워크 구축하려함. 필요한 최소비용을 출력하라
    - 모든 컴퓨터를 연결할 수 없는 경우는 없다
[S]
노드가 모두 연결되있어야 하는데 최소 비용이 들어야 한다.
    - 최소 신장 트리
    - 크루스칼 알고리즘
[L]
1. 크루스칼 알고리즘
    - param : edges(list) _ (cost,a,b) 형태로 저장 // queue(deque)
    - 서로소 자료구조 사용 : find_parent, union_parent 
        - variable : parent(list) _ 0으로 초기화 _ 개수는 node + 1
    - logic
        1) edges 정렬(cost)
        2) 가장 비용이 작은 값 queue에 담아
        3) while queue
        4) queue.popleft() -> 같은 그룹인지 체크(사이클 유무 확인) -> 아니면 ret에 cost 더하고 union하고 
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
# graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
costs = []
ret = 0

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    costs.append((c, a, b))

costs.sort()

for cost in costs:
    c, a, b = cost

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ret += c

print(ret)
