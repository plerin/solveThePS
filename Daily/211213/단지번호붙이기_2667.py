'''
>> P
N*N(정사각형) 지도가 있고 이 중 연결된 단지 별 집의 수를 반환하라
    - 상하좌우로 연결 == 연결된 단지
    - 1 : 집 // 0 : 집 없
    - 결과는 오름차순 출력
>> S
connected component 유형
dfs / bfs 모두 풀이 가능 
1. N과 해당하는 2차원 배열을 입력 받는다 -> graph(list), N(int)
2. N*N을 탐색하며 연결된 단지 확인 및 연결 단지 수 반환 -> ans(list)
3. 결과를 오름차순으로 반환 -> print(sorted(ans), sep='\n')
'''
from collections import deque


def dfs(x: int, y: int):

    if 0 <= x and x < N and 0 <= y and y < N and graph[x][y] == 1:
        ret = 1
        graph[x][y] = 0
        ret += dfs(x-1, y)
        ret += dfs(x+1, y)
        ret += dfs(x, y-1)
        ret += dfs(x, y+1)

        return ret

    return 0


def bfs(x: int, y: int):
    if graph[x][y] == 0:
        return 0

    ret = 1
    queue = deque([(x, y)])
    graph[x][y] = 0

    while queue:
        (x, y) = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                ret += 1

    return ret


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = []

for i in range(N):
    for j in range(N):
        ans.append(dfs(i, j))

ans = list(filter(lambda x: x != 0, ans))

print(len(ans), *sorted(ans), sep="\n")
