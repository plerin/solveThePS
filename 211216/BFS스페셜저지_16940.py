'''
>> P 
1~N까지 정점이 있고 N-1개 간선이 있을 때 주어진 트리가 BFS 여부 판단
    - 1) 시작 정점은 1 -> 방문 체크
    - 2) queue가 빌 때까지 반복
        - popleft()
        - 연결된 정점 queue에 모두 넣고 방문 처리
    - 3) 방문 순서는 중요하지 않아 BFS여부 판단이 중요
>> S
BFS에서 하나의 노드에 여러 노드 방문하면 EX) 1 : [2,3]
    -> 방문 체크 후 다음으로 넘어갈 때 방문 미체크(TRUE->FALSE)필요
2. 다른 방법으로는 트리를 보고 중간에 틀리면 0리턴 때리고 결과 출력
'''
from itertools import permutations
from collections import deque


def bfs(start: int):
    global visit
    ret = [1]

    queue = deque([start])
    visit[start] = True

    while queue:
        v = queue.popleft()

        for node in graph[v]:
            if visit[node]:
                continue
            visit[node] = True
            queue.append(node)
            ret.append(node)

    return ret


if __name__ == "__main__":

    N = int(input())
    graph = [[] for _ in range(N+1)]
    visit = [False] * (N+1)

    for _ in range(N-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    tree = list(map(int, input().split()))
    order = [0] * (N+1)

    # 입력 트리의 값을 인덱스로 우선순위를 값으로 order 갱신
    for i in range(len(tree)):
        order[tree[i]] = i

    # order(idx=요소 값, val=우선순위)로 graph 정렬
    for i in range(1, len(graph)):
        graph[i].sort(key=lambda x: order[x])

    ret = bfs(1)

    if ret == tree:
        print(1)
    else:
        print(0)
