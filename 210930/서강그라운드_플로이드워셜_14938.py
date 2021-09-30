
'''
0. 라이브러리 추가 _sys - 입력받기
1. 입력 받기 _ n,m,r , 아이템수 -> items n+1
2. graph 초기화
    1) 모든 요소 INF -> 2중배열 n+1
    2) i==f -> 0으로 채우기
    3) 입력 받은 값으로 채우기
3. 플로이드워셜 알고리즘 _ 3중 반복문 _ 점화식 : Dab = min(Dab, Dak, Dkb)
4. 결과 표출 _ sum()

'''
import sys

INF = sys.maxsize

# 1
n, m, r = map(int, sys.stdin.readline().split())
# item = [0 for _ in range(n+1)]
item = list(map(int, sys.stdin.readline().split()))

# for i in range(n+1):
#     item =

# 2
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(r):
    f, t, c = map(int, sys.stdin.readline().split())
    graph[f][t] = c
    graph[t][f] = c

# 3
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)
# 4
ret = 0
for i in range(1, n+1):
    add = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            add += item[j-1]
    ret = max(ret, add)

print(ret)
