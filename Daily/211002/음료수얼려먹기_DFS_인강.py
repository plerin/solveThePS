'''
n*m 그래프에서 상하좌우 찾아가며 아이스크림 개수 구하기
0. 라이브러리 입력 _ sys - 입력
1. 입력 받기
    1) 그래프 초기화 [] 만들고 그 안에 리스트 입력받아 
2. 방향벡터 초기화
    1) dx,dy 
3. graph 돌며 재귀호출
4. 결과 출력 
'''
# import sys


# def dfs(x, y):
#     if graph[x][y] == 1:
#         return False
#     graph[x][y] = 1

#     for i in range(4):
#         nx, ny = dx[i]+x, dy[i]+y
#         if nx < 0 or nx >= n or ny < 0 or ny >= m:
#             continue
#         if graph[nx][ny] == 1:
#             continue
#         if graph[nx][ny] == 0:
#             dfs(nx, ny)

#     return True


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False


# 1
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ret = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if dfs(i, j):
            ret += 1

print(ret)
