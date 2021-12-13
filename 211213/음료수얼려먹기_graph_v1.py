'''
2차원 배열, graph가 입력 값으로 주어짐
상하좌우로 연결 -> x+1,x-1,y+1,y-1

dfs
1. n*m 그래프를 탐색하며 해당 위치 값이 0인경우 함수 호출
2. 방문처리하고 x,y 값이 2차원 배열안에 해당할 경우(0<=x<n, 0<=y<m) 방문처리(graph[x][y]=1) 후 재귀호출 아니면 return False
    - param x:int, y:int 
    - return : Ture/False
'''


def dfs(x: int, y: int):
    global n, m
    if 0 <= x and x < n and 0 <= y and y < m and graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans += 1

print(ans)
