'''
>> P
N*M 크기 얼음 틀이 있고 구멍(0), 칸막이(1)로 표시됨
구멍 뚫려 있는 부분끼리 상하좌우로 연결되어 있음
생성되는 총 아이스크림 개수를 구하라
    - 범위 : N,M ~ 1000
>> S
알고리즘
2차원 배열에서 상하좌우 연관됨 -> DFS/BFS 풀이

접근
1. 얼음틀(N*M)의 모든 요소를 돌며 '0'인 경우 함수 호출
2. 상하좌우 이동하며 '0' -> '1'처리하고 없으면 True리턴
3. True리턴 받으면 ans+=1 
4. 결과 출력

코드
1. 이차원 배열로 입력 받음
2. 2차원 배열 반복하며 요소 확인
    - if frame[i][j] == 0 then call method and ans+=1

3. 메소드 생성
def dfs(x: int, y: int) -> boolean:
    if 0 <= x < n and 0 <= y < m and frame[x][y] == 0:
        frame[x][y] = 1

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    
    return True

from collections import deque
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x: int, y: int) -> boolean:
    queue = deque([(x, y)])
    frame[x][y] = 1

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and frame[nx][ny] == 0:
                queue.append((nx, ny))
                frame[nx][ny] = 1
    return True
'''
from collections import deque
from xmlrpc.client import Boolean


def dfs(x: int, y: int) -> Boolean:
    # 이동 범위가 범위 안에 있으며 '0'인 경우
    if 0 <= x < n and 0 <= y < m and frame[x][y] == 0:
        # 방문 처리
        frame[x][y] = 1

        # 상하좌우 위치 재귀 호출
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True
    else:
        return False


def bfs(x: int, y: int) -> Boolean:
    if frame[x][y] == 1:
        return False

    # 큐에 담아 인접 노드 방문 진행
    queue = deque([(x, y)])
    frame[x][y] = 1

    while queue:
        x, y = queue.popleft()

        # move를 통해서 좌표 이동(x, y)
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            # 범위에 포함되어 있으며 '0'인 경우만 진행
            if 0 <= nx < n and 0 <= ny < m and frame[nx][ny] == 0:
                queue.append((nx, ny))
                frame[nx][ny] = 1
    return True


n, m = map(int, input().split())
frame = [list(map(int, input())) for _ in range(n)]

# bfs 상하좌우 좌표이동 위함
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j):
            ans += 1

print(ans)
