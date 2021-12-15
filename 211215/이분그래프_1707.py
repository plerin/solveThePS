'''
>> P
그래프에서 두 그룹으로 나눈 정점이 서로 인접하지 않은 경우로 분할할 수 있다면 이분 그래프(Bipartie Graph)라고 함
그래프가 주어졌을 때 이분 그래프인지 여부 판단하여 출력하라
    - V, E : 정점 수, 간선 수 // ~2만, ~20만
>> S
이분 그래프 파악 방법
    - 인접 노드를 방문할 때마다 서로 다른 색으로 칠하기
    - DEFAULT : 0 & 1 // -1
DFS 풀이 방법
    - 초기 방문 값을 1/-1로 초기화하고 인접 노드 방문할 때마다 1 이면 -1로 // -1이면 1로
    - 인접 노드 값이 현재 값과 같을 때 NO 출력(return False)
    - base_condition : 인접 노드 값중 -1이 없으면 자연스럽게 끝남(return True)
BFS 풀이 방법
    - 초기 방문 값을 1/-1로 초기화하고 인접 노드를 모두 현재 노드 색상의 반대 값을 칠함
    - 만약 인접 노드 값이 현재 값과 같을 때 NO 출력
'''

from collections import deque
import sys

input = sys.stdin.readline


def dfs(v: int):
    stack = [v]

    if node[v] == 0:
        node[v] = 1

    while stack:
        v = stack.pop()

        for i in graph[v]:
            if node[i] == 0:
                node[i] = node[v] * (-1)
                stack.append(i)
            elif node[i] == node[v]:
                return False

    return True


def dfs2(v: int):
    global node

    if node[v] == 0:
        node[v] = 1

    ret = True

    for i in graph[v]:
        if node[i] == 0:
            node[i] = node[v] * (-1)
            ret = dfs(i)

            if not ret:
                ret = False
                break
        elif node[v] == node[i]:
            return False

    return ret


def bfs(v: int):
    queue = deque([v])

    if node[v] == 0:
        node[v] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if node[i] == 0:
                node[i] = node[v] * (-1)
                queue.append(i)
            elif node[i] == node[v]:
                return False

    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    node = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_want = True
    for i in range(1, V+1):
        if not dfs(i):
            is_want = False
            break
    print("YES" if is_want else "NO")
