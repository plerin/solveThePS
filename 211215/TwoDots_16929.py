'''
>> P
N*M인 게임판 위에서 사이클 존재 여부 확인하라
    - 사이클 조건
        1) 점 4개 이상 구성
        2) 같은 색 정점이 인접한 형태로 이어져있어야 한다
>> S
사이클 여부
2차원 배열에서 사이클을 어떻게 확인하는지?
    - connected_component로 False -> True로 만드는데 BFS로 바꿔나가는 과정에서 다음 칸이 이미 True로 바뀌어 있다면
    == 4개이상 && 사이클 있음
각 요소를 False로 초기화할 list 만들고 방문할 때마다 False -> True
    - 방문 조건은 N*M 안에 있어야하고 출발 노드와 알파벳이 같고 False 이여야 함!

'''
from collections import deque


def bfs(x: int, y: int):
    global graph, check

    if check[x][y] != 0:
        return False

    queue = deque([(x, y)])
    check[x][y] = graph[x][y]+str(0)    # 0 값에 영문자 알파벳을 붙여 갱신

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == graph[x][y]:
                if check[nx][ny] == 0:  # 처음 방문한다면
                    check[nx][ny] = graph[nx][ny] + \
                        str(int(check[x][y][1:]) + 1)
                    queue.append((nx, ny))
                # 다른 값에 의해 이미 방문했고 그 값이 이전 값이 아니라면 == 사이클 존재
                elif int(check[nx][ny][1:]) > int(check[x][y][1:]):
                    return True

    return False


N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if bfs(i, j):
            print("Yes")
            exit()

print("No")
