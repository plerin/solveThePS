'''
goal : N*M 얼음 틀에서 총 아이스크림 개수를 구하라
    1) 0 : 구멍, 1 : 칸막이
    2) 상/하/좌/우로 연결되어 있다.
0. 라이브러리 추가 : sys(입력), deque(queue)
1. 입력받기
    1)  N,M : 행과 열(N*M 이중 배열)
    2) 행렬을 구성하는 행단위
2. 로직
    1) 변수 : frame에 행렬 입력, visited (2중배열, False초기화)
    2) 방향벡터 : 상하좌우 움직이기 위함 dx,dy
    3) 행열 모든 요소에 대해 bfs 함수 호출(리턴은 true/false)
    4) deque에 담고 상하좌우로 살펴가며 boolean반환
3. 결과 반환
'''
# 0
import sys
from collections import deque


def bfs(i, j):
    if graph[i][j] == 1:
        return False

    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        graph[x][y] = 1
        for i in range(4):
            cx, cy = x+dx[i], y+dy[i]
            if cx < 0 or cx >= N or cy < 0 or cy >= M:
                continue
            if graph[cx][cy] == 1:
                continue
            q.append((cx, cy))

    return True


def dfs(i, j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True

    return False


# 1
N, M = map(int, input().split())
graph = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))

ret = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ret += 1

print(ret)
