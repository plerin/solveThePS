'''
>> P
N*M 직사각형 미로에서 탈출해야 한다
괴물이 있는 위치(0) 없는 위치(1)이고 한 번에 한 칸씩 이동
현재 (1,1)에 있으며 출구는 (N,M)이라고 할 때 최소 칸 개수 구하라

>> S
알고리즘
2차원 배열이고 비용이 같을 때(한 번에 한칸씩) 최소 칸의 개수 
=> BFS (시간/공간 복잡도 문제 없어)

접근
1. bfs 준비물 구하기
    deque, move(dx,dy), 방문처리 어떻게? elem 값을  이전값 + 1로 갱신하며 진행(그래야 최소 칸 알 수 있어)
2. 주의 사항
    인덱스를 0~n-1 이 아닌 1~n으로 사용

코드
1. 준비물
from collection ..

2. 함수 호출
escape_

def escape_maze(x, y) # param : 출발 좌표(x,y)
    queue = deque()
    
    while queue:
        x, y = popleft()
        
        for dx, dy in move:
            nx, ny
            
            if 범위 포함, 1인지여부 확인:
                range = 1
                queue.append()
3. 출력 
print(maze[n-1][m-1])
'''

from collections import deque


def escape_maze(x: int, y: int) -> None:
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 좌표(x,y) 상하좌우 이동
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

print(escape_maze(0, 0))
