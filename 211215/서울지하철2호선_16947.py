'''
>> P
51개 정거장과 51개 양방향 간선으로 이루어진 지하철 2호선이 있다.
각 역과 순환선 사이의 거리를 구하라
    - 역(A)과 순환선 사이 거리 = A와 순환선 속한 역 사이 거리 중 최솟값
    - 역은 1~N번까지 번호로 주어진다.
>> S
역과 순환선 사이 최소 값을 구하는 방법
    - 모든 역에서 다른 역까지의 거리를 구해(bfs) 그 과정에서 순환역이면(출발 역으로 돌아오는 경우) 리스트에 저장
        -> distance[station] = 1 초기화하고 나머지 값들 갱신
    - 모든 역을 반복하며 순환역까지의 거리 중 가장 작은 값 저장
        -> min(list(filter(lambda x: x in circul, distance[st]))) 
'''
from collections import deque


def bfs(start: int):
    global distance

    queue = deque([start])
    distance[start][start] = 1
    is_loop_line = False

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if distance[start][i] == 0:
                distance[start][i] = distance[start][now] + 1
                queue.append(i)
            elif i == start and distance[start][now] != 2:
                # if distance[start][i] > distance[start][now]:
                print(start, distance[start][i], distance[start][now])
                is_loop_line = True
                continue

    return is_loop_line

# def dfs(start: int, next_node: int):

#     for i in graph[start]:
#         if distance[start][i] == 0:
#             distance[start][i] = distance[next_node][]


N = int(input())
graph = [[] for _ in range(N+1)]
distance = [[0] * (N+1) for _ in range(N+1)]
circul_line = []

for _ in range(N):
    st1, st2 = map(int, input().split())
    graph[st1].append(st2)
    graph[st2].append(st1)

for i in range(1, N+1):
    if bfs(i):
        circul_line.append(i)
# bfs(1)

print(distance)
print(circul_line)
