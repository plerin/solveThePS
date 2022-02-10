'''
>> P
1~N역이 있는데 각 역에서 순환역까지 최소 경로를 출력하라
    - 정점과 간선의 수가 같다
    - 순환선 = 한 역에서 출발해서 계속 가면 다시 출발한 역으로 돌아올 수 있는 노선
    - 두 역 사이의 거리는 지나야 하는 간선의 수
    - 역과 순환선 사이 거리는 순환선 역 거리의 최솟값
>> S
1. 순환선 여부는 DFS로 풀이
    - 출발역, 현재역, 거리를 파라미터로 하고 현재역의 다음 역이 출발역과 같고 거리가 3이상인 경우 == 순환선
    - 순환선인 경우는 global 리스트에 저장해 놓기
2. 역 간 거리는 BFS로 풀이
    - 현재 역에서 다른 역까지의 거리를 모두 구하기
    - 순환역 중 거리가 가장 짧은 거리를 출력
        -> 순환역 가리기 -> filter && 짧은 거리 -> min()
'''

from collections import deque
import sys

sys.setrecursionlimit(10**9)    # 재귀깊이설정 최대 값(기본 값 1000)
input = sys.stdin.readline


def check_cycle(start: int, cur: int, cnt: int):
    global is_cycle
    ret = False

    if start == cur and cnt >= 3:
        is_cycle.append(start)
        return True

    for vec in graph[cur]:
        if not visit[vec]:
            visit[vec] = True
            ret = check_cycle(start, vec, cnt+1)
            visit[vec] = False
        # 다음 노드가 출발 노드와 같고 거리가 3이상인 경우(참고, 출발 노드 다음노드가 거리 ==2)
        elif vec == start and cnt >= 3:
            # print(start, cur, visit)
            ret = check_cycle(start, vec, cnt)

        if ret == True:
            return True
    return False
# 인접 노드 탐색하다가 순환선 안에 있는 노드면 리턴


def get_dist(start: int):
    global dist
    dist_per_node = [0] * (N+1)

    queue = deque([start])
    dist_per_node[start] = 1

    while queue:
        now = queue.popleft()

        if now in is_cycle:
            dist[start] = dist_per_node[now]-1
            return
        for vec in graph[now]:
            if dist_per_node[vec] == 0:
                dist_per_node[vec] = dist_per_node[now] + 1
                queue.append(vec)


N = int(input())
graph = [[] for _ in range(N+1)]
dist = [0] * (N+1)
visit = [False] * (N+1)
is_cycle = list()

for _ in range(N):
    st1, st2 = map(int, input().split())
    graph[st1].append(st2)
    graph[st2].append(st1)


for i in range(1, N+1):
    visit[i] = True
    check_cycle(i, i, 1)
    visit[i] = False

for i in range(1, N+1):
    get_dist(i)

print(*dist[1:])
