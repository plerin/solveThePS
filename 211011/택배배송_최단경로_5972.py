'''
goal : 현서가 찬홍이에게 가는 길에 만나는 소의 여물을 주는 최소 비용 구하기
    1) N,M의 범위가 크다 -> 플루이드 워셜 X
    2) 최단 경로(비용) 구하기
0. 라이브러리 추가 _ sys(입력), heapq
1. 입력 받기
    1) N,M : 노드와 간선의 수
    2) FROM, TO, COST : 시작 / 도착 / 비용
2. 로직
    1) 변수 : graph(인접노드 추가), distance(방문여부 체크 _ INF 로 초기화)
    2) 다익스트라 알고리즘 : HEAPQ를 활용
3. 결과출력
'''

# 0
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def shortestPath(s):
    q = [(0, s)]
    distance[s] = 0

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for i in graph[node]:
            cc = cost + i[1]
            if cc < distance[i[0]]:
                distance[i[0]] = cc
                heapq.heappush(q, (cc, i[0]))


# 1
N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))
    graph[to].append((fr, cost))

# 2
shortestPath(1)

print(distance)
# 3
print(distance[N])
