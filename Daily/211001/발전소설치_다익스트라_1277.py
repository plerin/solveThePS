'''
0. 라이브러리 추가 _ sys - 입력,최댓 값, heapq - 우선순위 큐
1. 입력 받기 _ N,W (노선/간선), M : 길이 제한
2. 그래프, 거리 리스트 초기화
    1) 그래프 - 1~N까지 주어진 좌표(이중배열) _ X,Y 좌표에 값 입력 나머지는 0
    2) 거리 값 : N+1개 INF로 초기화
3. 다익스트라 호출 _ START = 1의 X,Y 좌표
4. 결과 출력 _ *1000 하고 버림
'''
import sys
import heapq
import math

INF = sys.maxsize


def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, vec = heapq.heappop(q)

        if distance[vec] < dist:
            continue

        for i in graph[vec]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


n, w = map(int, sys.stdin.readline().split())
m = float(input())

graph = [[] for _ in range(n+1)]  # 일단 만들고 제한 거리에 맞춰 인접노드 추가하자
distance = [INF] * (n+1)
pos = []

for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().split())
    pos.append((x, y))
    # pos[x][y] = i

for i, v1 in enumerate(pos):
    for v2 in pos[i+1:]:
        j = pos.index(v2)
        # 두 점 사이가 m보다 작으면 그래프 인접행렬로 추가
        dist = ((v2[0]-v1[0])**2+(v2[1]-v1[1])**2)**0.5
        if dist <= m:
            graph[i+1].append((dist, j+1))

# middle = 0

# for _ in range(w):
#     f, t = map(int, sys.stdin.readline().split())
#     # pos[f-1]
#     print(pos[f-1], pos[t-1])
#     dist = ((pos[t-1][0]-pos[f-1][0])**2+(pos[t-1][1]-pos[f-1][1])**2)**0.5
#     middle += dist

mv = 0

for _ in range(w):
    f, t = map(int, sys.stdin.readline().split())
    mv = max(mv, t, f)

dijkstra(1)

total = math.trunc(distance[n]*1000)
part = math.trunc(distance[mv]*1000)

# print(middle)
# part = math.trunc(middle*1000)

# print(distance[n])

print(total-part)
