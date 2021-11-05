'''
[P]
N명의 학생을 키 순서대로 줄 세우는 프로그램
[S]
N(노드), M(간선)으로 구성된 방향성 그래프
    -> 유형 : 위상정렬(사이클 없는 방향성 간선을 갖은 그래프에서 순서대로 나열 )
[L]
1. 학생 별 indegree를 구하고 위상 정렬로 풀이(queue)
    0) deque 라이브러리 추가
    1) 학생 수 +1 크기의 리스트를 0으로 초기화
    2) greph 간선 (a -> b) 입력 받기 _ b의 ingegree +=1
    3) queue에 indegree 0인 항 넣고 계산
    4) 
'''

from collections import deque
import sys

input = sys.stdin.readline


def topology_sort():
    global graph
    global indegree

    queue = deque([])
    ans = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        ans.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)
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
