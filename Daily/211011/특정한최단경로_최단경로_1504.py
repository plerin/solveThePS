# '''
# goal : 1->N을 갈 때 반드시 특정 두 정점을 거치면서 이동하는 최단경로를 구하라
#     1) 각 노드 간 양방향성 그래프를 갖는다
#     2) 거쳐가야 하는 두 정점을 V1,V2라고 한다
# 0. 라이브러리 추가 _ sys(입력), heapq
# 1. 입력 받기
#     1) N,E : 노드 수와 간선 수
#     2) 두 노드 간 이동 비용 : from, to, cost
# 2. 로직
#     1) 변수 선언 : graph(인접노드 비용 입력), distance(출발노드로 부터 최단 경로 , INF로 초기화)
#     2) 다익스트라 알고리즘 적용 : HEAPQ 활용
# 3. 결과 출력
#     1) 두 경로 중 최단 경로 선택 : 1->V1->V2->N / 1->V2->V1->N
#     2) 경로 없으면 -1 출력
# '''
# # 0
# import sys
# import heapq

# input = sys.stdin.readline
# # INF = float('inf')
# INF = sys.maxsize

# def shortestPath(s):
#     if s == 1:
#         d = distance1
#     elif s == V1:
#         d = distance2
#     elif s == V2:
#         d = distance3

#     q = [(0, s)]
#     d[s] = 0

#     while q:
#         cost, now = heapq.heappop(q)

#         if d[now] < cost:
#             continue

#         for i in graph[now]:
#             cc = cost + i[1]
#             if cc < d[i[0]]:
#                 d[i[0]] = cc
#                 heapq.heappush(q, (cc, i[0]))


# # 1
# N, E = map(int, input().split())
# graph = [[] * (N+1) for _ in range(N+1)]
# distance1 = [INF] * (N+1)
# distance2 = [INF] * (N+1)
# distance3 = [INF] * (N+1)

# for _ in range(E):
#     fr, to, cost = map(int, input().split())
#     graph[fr].append((to, cost))
#     graph[to].append((fr, cost))

# V1, V2 = map(int, input().split())
# # 2
# shortestPath(1)
# shortestPath(V1)
# shortestPath(V2)

# # 3
# ret = min(distance1[V1]+distance2[V2]+distance3[N],
#           distance1[V2]+distance3[V1]+distance2[N])

# if ret >= INF:
#     print(-1)
# else:
#     print(ret)


'''
goal : 1->N을 갈 때 반드시 특정 두 정점을 거치면서 이동하는 최단경로를 구하라
    1) 각 노드 간 양방향성 그래프를 갖는다
    2) 거쳐가야 하는 두 정점을 V1,V2라고 한다
0. 라이브러리 추가 _ sys(입력), heapq
1. 입력 받기
    1) N,E : 노드 수와 간선 수
    2) 두 노드 간 이동 비용 : from, to, cost
2. 로직
    1) 변수 선언 : graph(인접노드 비용 입력), distance(출발노드로 부터 최단 경로 , INF로 초기화)
    2) 다익스트라 알고리즘 적용 : HEAPQ 활용
3. 결과 출력
    1) 두 경로 중 최단 경로 선택 : 1->V1->V2->N / 1->V2->V1->N
    2) 경로 없으면 -1 출력
'''
# 0
import sys
import heapq

input = sys.stdin.readline
# INF = float('inf')
INF = sys.maxsize


def shortestPath(s):
    d = [INF] * (N+1)

    q = [(0, s)]
    d[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        if d[now] < cost:
            continue

        for i in graph[now]:
            cc = cost + i[1]
            if cc < d[i[0]]:
                d[i[0]] = cc
                heapq.heappush(q, (cc, i[0]))
    return d


# 1
N, E = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(E):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))
    graph[to].append((fr, cost))

V1, V2 = map(int, input().split())
# 2
d1 = shortestPath(1)
d2 = shortestPath(V1)
d3 = shortestPath(V2)

# 3
ret = min(d1[V1]+d2[V2]+d3[N],
          d1[V2]+d3[V1]+d2[N])

if ret < INF:
    print(ret)
else:
    print(-1)
