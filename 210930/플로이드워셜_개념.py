# 무한 값 정의_10억
INF = int(ie9)

# n= 노드, m = 간선
n, m = map(int, input().split())
# 그래프는 노드 +1 만큼 만들고 모든 요소(element)는 INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보 입력 받아 그 값으로 초기화
for _ in range(m):
    f, t, c = map(int, input().split())
    graph[f][t] = c

# 플로이드 워셜 알고리즘 , A->B 비용을 'A->B' / 'A->K + K->B' 비용 중 MIN 값으로 입력
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
        print()
