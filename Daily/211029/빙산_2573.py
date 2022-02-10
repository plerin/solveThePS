'''
[P]
빙산이 분리되는데 걸리는 최초 시간(년)을 반환
    - 0 : 바다 // 0이 아닌 수 : 빙산 높이
    - 동/서/남/북으로 둘러쌓인 빙산은 바다(0)과 만나는 수 만큼 줄어든다
[S]
그래프(2차원)에서 인접한 노드에 영향을 받아 분리되는 최초의 시간 == 최소 값
    - 유형 : 그래프 탐색(BFS) _ 노드간 거리가 일정(1)
[L]
1. 입력 받기
    - N(int) : 행  // M(int) : 열
    - graph(list)
2. BFS 풀이 준비물
    - 라이브러리 _ DEQUE
    - 방향벡터 _ dx(list) / dy(list) : 상하좌우의 영향을 받기 때문에
3. 빙하 있는 좌표 모아놓기
    - graph 반복하며 '0'이 아닌 좌표를 queue(deque) 에 입력
4. 합수 호출
    - param : queue
    - logic :
        1) year = 0 
        2) while queue -> v = popleft() -> for i in range(len(dx))  -> nx,ny 의 값이 '0'이면 -1 
        3) 빙산 분리 여부 체크 -> 이걸 함수로 하자 모든 요소 반복하며 coonected-component 개수 확인
        4) 2,3 반복 만약 모두 0될때까지 분리 안 됐으면 0 반환 아니면 year
5. 결과 출력
'''

from collections import deque
import sys

sys = sys.stdin.readline


# def count_ice_mountain(graph):
#     cnt = 0
#     visited = [0] *
#     for i in range(graph):
#         for j in range(graph[i]):
#             if graph[i][j] != 0:

def count_glacier(queue):


def melt_glacier(queue):
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if graph[nx][ny] == 0:
                if graph[x][y] == 1:
                    graph[x][y] = -1
                else:
                    graph[x][y] -= 1


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = deque([])

while True:
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                queue.append([i, j])
                visited[i][j] = 1
    # 커넥티드 _ 빙하 수 카운트
    a = count_glacier(visited)

    # 멜팅 _ 1년 동안 녹아
    melt_glacier()

    # 커넥티드 _ 빙하 수 카운트
    b = count_glacier()

    # if a != b and b
    if b == 0:
        print(0)
    elif a != b:
        pass

if len(queue) == 0:
    print(0)
    exit()


print(graph)
