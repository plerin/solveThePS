'''
0. 라이브러리 추가 _ deque - bfs에서 사용
1. 입력 받기 _ n*m
2. graph, visited 초기화
    1) graph는 입력 받는 값으로
    2) visited는 필요없겠다.1인곳만 방문할거니까 
3. 모든 노드 방문하며 bfs할 필요 없음 미로 찾기는 결국 다 이어져 있다는 말이니까 예외조건 없다면
4. 결과 출력 _ graph[n-1][m-1]
'''
from collections import deque


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))


# 1
n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# 2
graph = [list(map(int, input())) for _ in range(n)]

# 3
bfs(0, 0)

# 4
print(graph[n-1][m-1])
