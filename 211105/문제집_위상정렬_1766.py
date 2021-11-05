'''
[P]
난이도 순서대로 1~N번까지 있는 문제집을 풀려고한다. 풀 문제의 순서를 결정해 주는 프로그램 작성
    - 1. N개 모두 풀어야 한다.
    2. 먼저 푸는 것이 좋은 문제가 있으면 먼저 풀어야 한다.
    3. 가능하면 쉬운 문제부터 풀어야 한다.
[S]
이런 유형은 문제가 어렵다기 보다 이 문제를 보고 적절한 풀이 방법을 떠올리는 게 핵심
방향이 있는 문제(난이도) 중에서 먼저 풀 수 있는 문제를 먼저 풀면서 모두 풀어야 한다고 하면 유형은 '위상정렬'
    - 위상 정렬 알고리즘을 활용한 풀기
    - 특징적인 건 1~N까지 난이도 순서대로 정렬 됐으니 정답이 여러 개가 아님
'''

# from collections import deque
import heapq
import sys

input = sys.stdin.readline


def topology_sort():
    global graph
    global indegree

    queue = []
    ans = []

    for i in range(1, len(indegree)):
        if indegree[i] == 0:  # i가 1부터 시작 == 난이도가 낮은 문제부터 입력
            heapq.heappush(queue, i)
            # queue.append(i)

    while queue:
        # now = queue.popleft()
        now = heapq.heappop(queue)
        ans.append(now)

        for i in sorted(graph[now]):  # 인접 노드(문제)가 여러 개일 때 정렬해서 반복 == 난이도가 낮은 문제부터 들어가
            indegree[i] -= 1
            if indegree[i] == 0:
                # queue.append(i)
                heapq.heappush(queue, i)

    return ans


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

ret = topology_sort()

print(*ret)
