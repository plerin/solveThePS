

# def dfs(i, j):
#     if i < 0 or i >= n or j < 0 or j >= m:
#         return False

#     if frame[i][j] == 0:
#         frame[i][j] = 1
#         dfs(i-1, j)
#         dfs(i+1, j)
#         dfs(i, j-1)
#         dfs(i, j+1)
#         return True

#     return False


# n, m = map(int, input().split())
# frame = []
# ret = 0

# for _ in range(n):
#     frame.append(list(map(int, input())))

# for i in range(n):
#     for j in range(m):
#         if dfs(i, j):
#             ret += 1

# print(ret)


# DFS
def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True

    return False


n, m = map(int, input().split())
graph = []
ret = 0
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ret += 1

print(ret)


# BFS
# from collections import deque


# def bfs(i, j):
#     if graph[i][j] == 1:
#         return False

#     queue = deque([(i, j)])

#     while queue:
#         x, y = queue.popleft()
#         graph[x][y] = 1

#         for i in range(4):
#             dn = x + dx[i]
#             dm = y + dy[i]

#             if dn < 0 or dn >= n or dm < 0 or dm >= m:
#                 continue
#             if graph[dn][dm] == 1:
#                 continue
#             if graph[dn][dm] == 0:
#                 queue.append((dn, dm))
#     return True


# n, m = map(int, input().split())
# graph = []
# ret = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(n):
#     graph.append(list(map(int, input())))

# for i in range(n):
#     for j in range(m):
#         if bfs(i, j):
#             ret += 1

# print(ret)
