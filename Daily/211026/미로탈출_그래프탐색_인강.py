'''
[P]
N*M 직사각형 형태의 미로에서 괴물을 피해 탈출할 때 최소 칸의 개수
    - 시작 위치 (1,1) / 미로의 출구 (N,M)
    - 한 칸씩 이동 
    - 0 : 괴물 // 1: 괴물 없음
[S]
그래프 탐색(Graph-Search) 유형으로 최소 칸의 개수 == BFS 이용
    - 방향벡터로 이차배열 이동하며 요소 값 갱신(이전 요소 값+1)
[L]
0. 라이브러리 호출 _ from collections import deque
1. 입력 값을 통해 변수 선언 _ N(int),M(int),maze(list)
2. 필요 변수 선언 _ dx(list),dy(list) _ 상하좌우 움직일 수 있도록
3. 시작 위치를 인자로 함수 호출
4. 함수 선언
    - PARAM : x(int),y(int)
    - LOGIC :
        1) deque를 사용하여 출발지 입력
        2) loop with deque -> popleft()
        3) 방향벡터를 반복하며 다음 좌표 생성(nx,ny)
        4) N*M 안에 있는지 여부 체크
        5) 해당 좌표 값이 '1'이라면 현재 값+1로 값 갱신하고 deque에 담기
    - RETURN : NONE
5. 결과 값 출력 [N-1][M-1] 
'''

from collections import deque


def bfs(start):
    q = deque([start])

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                q.append((nx, ny))


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


bfs((0, 0))

print(maze[N-1][M-1])
