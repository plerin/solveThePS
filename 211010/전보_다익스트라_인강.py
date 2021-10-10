'''
goal : N개의 도시에서 m개의 통로를 퍼져나갈 때 도시 총 개수와 시간 반환
    1) N,M의 범위가 커서 플로이드 워셜 사용 못함
    2) 출발점 c
0. 라이브러리 추가 _ sys(입력), heapq(우선순위 큐)
1. 입력 받기
    1) N M C : 도시 개수 / 통로 개수 / 출발 도시
    2) F T C : 출발 도시 / 도착 도시 / 비용
2. 다익스트라 알고리즘
    1) 변수 선언 :  graph(경로와 비용 담음), distance(INF로 초기화) 
    2) 함수 : 파라미터(출발 도시)
        1) 큐에 담고 거리 갱신
        2) 큐 반복하며 heappop()으로 추출
        4) 기존 거리와 비교
        5) 인접 노드 불러와 거리 갱신
'''
import heapq
import sys


def dijkstra(s):
    q = [(0, s)]
    distance[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            cc = cost + i[1]
            if cc < distance[i[0]]:
                distance[i[0]] = cc
                heapq.heappush(q, (cc, i[0]))


# 0

input = sys.stdin.readline
INF = float('inf')
# 1
N, M, S = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    f, t, c = list(map(int, input().split()))
    graph[f].append((t, c))
    # graph[f][t] = c
    # graph[t][f] = c

# 2
dijkstra(S)

ret = []

for i in distance:
    if i == INF:
        continue
    ret.append(i)

print(len(ret)-1, max(ret))
