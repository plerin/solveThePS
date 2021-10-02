'''
goal : 방향없는 그래프(양방향), 연결 요수 개수 구하라
1. 입력 받기 _ n,m(노드,간선)
2. graph,visited 초기화 _ n+1개로 0은 사용하지 않는다
3. 그래프 돌며 dfs 호출 시 true면 ret+=1
4. 결과 출력
'''


def dfs(node):
    if visited[node] == True:
        return False
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

    return True

    # 1
n, m = map(int, input().split())
# 2
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
# 3
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    # graph[v].append(u)
# 4
ret = 0
for node in range(1, n+1):
    if dfs(node) == True:
        ret += 1
# 5
print(ret)
