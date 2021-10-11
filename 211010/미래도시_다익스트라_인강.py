'''
goal : n개의 회사가 있고 그 사이 정해진 도로가 있다 1에서 k를 거처 X를 가는 최단 경로
    1) 도로의 비용은 1
    2) 도로는 양방향
    3) 최단 경로
    4) 1<=x<=100 (작은 범위) 
    => 플로이드 워셜 알고리즘 사용
0. 라이브러리 추가 _ sys(입력)
1. 입력 받기
    1) N M : 회사 개수와 경로 개수
    2) F T : 두 회사관 연결 관계
    3) X K : 목적지와 경유지
2. 로직 수행
    1) 변수 선언
        1) graph : i->i는 0입력, i->j 입력, 나머지는 INF
    2) 3중 반복문 : 모든 노드에서 각 노드 최단경로 점화식이용
        1) 점화식 : Aij = min(Aij, Aik, Akj)
    3) 결과 반환
        1) graph[0][x-1]
'''

# 0
import sys

input = sys.stdin.readline
INF = float('inf')

# 1
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    f, t = map(int, input().split())
    graph[f][t] = 1
    graph[t][f] = 1

X, K = map(int, input().split())


# 2
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# print(graph)
ret = graph[1][K]+graph[K][X]

if ret == INF:
    print(-1)
else:
    print(ret)
