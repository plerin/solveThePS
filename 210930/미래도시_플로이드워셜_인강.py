import sys
INF = sys.maxsize

# 입력 받기 N - 회사 , M - 경로, X = 목적지 , K = 경유지
n, m = map(int, input().split())
# graph 초기화
'''
1. 이중배열(N*N) 모든 요소를 INF로 초기ㅗ하
2. 노드자기자신(I==J)를 0으로 초기화
3. 입력 값 초기화(노드 간 거리) -> 양방향이니까 서로 1로 초기화
'''
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 적용 _ 3중 FOR문 (N+1)만큼, 점화식 이용
# 점화식 == D1X = MIN(D1X, D1K+DKX)
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a]+graph[a][c])

# graph[1][x] 값이 INF 이면 -1 아니면 그 값 반환
if graph[1][x] == INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])
