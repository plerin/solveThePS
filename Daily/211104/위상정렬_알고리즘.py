
from collections import deque


def topology_sort():
    # 정렬 결과 담을 리스트
    result = []
    q = deque()

    for i in range(1, v+1):
        # 진입차수 0인 경우 큐에 담기
        if indegree[i] == 0:
            q.append(i)
    # until queue is empty()
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            # now(노드)가 가르키는 노드의 인접차수 -1
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')


v, e = map(int, input().split())
# 모든 노드에 대해 진입차수 0으로 초기화
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a->b (방향성 있는경우) b의 진입차수 + 1
    indegree[b] += 1

topology_sort()
