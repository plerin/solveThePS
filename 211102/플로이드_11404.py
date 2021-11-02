'''
[P]
N(2~100)개의 도시가 있고 도시 간 이동하기 위한 버스가 M대 있다. A->B로 가는데 필요한 비용의 최솟 값을 구하라
[S]
N개의 노드와 M개의 간선으로 구성된 그래프(2차원)이 있고 2차원 배열 형태로 모든 노드에서 그 외 노드로 이동하는 최솟 값을 리턴
    - 유형 : 모든 노드에서 다른 노드로의 최솟 값을 구해야함 == 플로이드 워셜 노드의 범위도 (100이하)
    - 접근 : 그래프를 0으로 초기화 한 후 입력된 값으로 갱신하고 플로이드 워셜 알고리즘을 통해 시간복자도 O(N***3) 으로 2차원 배열으로 구한 뒤 출력
[L]
1. 입력 받기
    - n(int) : 도시 수 // m(int) : 버스 수
    - graph(list) : n*n 크기로 0으로 초기화 후 입력 된 값으로 갱신
2. 플로이드 워셜 수식 사용
    - 3중 반복문을 사용하여 graph 갱신
3. 결과 리턴 
'''
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for arr in graph:
    for e in arr:
        if e == INF:
            e = 0
        print(e, end=' ')
    print()
    # print(' '.join(arr))
