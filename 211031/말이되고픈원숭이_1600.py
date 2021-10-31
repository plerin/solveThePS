'''
[P]
말이 되고싶은 원숭이는 K번만 말처럼 이동하고 나머지는 동/서/남/북 1칸만 이동할 수 있다. 시작지점에서 도착지점가지 갈 수 있는 최소 동작
    - 시작위치 : [0][0] // 도착위치 [H-1][W-1]
[S]
인접 노드로 움직이고 최소 횟수를 구하라 == 그래프 탐색 BFS
    - 유형 : 그래프 탐색 (BFS)
[L]
1. 입력 받기
    - K(int) : 말 빙의 횟수
    - W(int) : 열 // H(int) : 행
    - graph(list) : 2차원 배열로 0은 평지 1은 장애물을 의미
2. BFS 준비물
    - 라이브러리 : sys(입력), deque(queue)
    - step(list) : 방향벡터인데 tuple 형태로 이동을 담아놔
3. BFS 함수 호출
    - argument : [0,0]
4. bfs 함수
    - 목적 : 주어진 좌표에서 목적지로 가는 데 걸리는 최소 이동 횟수
    - param : coord(list) x,y 좌표로 구성
    - logic
        1) queue에 좌표를 담아
        2) while queue
        3) for i in steps: -> 범위 체크 & 평지(0) 체크 & 만약 말처럼 이동하면 k -= 1 그러면서 이동할 지역 값 갱신
    - return : 
5. 결과 출력
'''
from collections import deque
import sys

input = sys.stdin.readline


def bfs(coord):
    queue = deque(coord)

    while queue:
        x, y = queue.popleft()

        for s in steps:
            nx, ny = x+s[0], y+s[1]

            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1


k = int(input())
W, H = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H)]
steps = [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, -1), (-2, 1),
         (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

graph[0][0] = 1

ret = bfs([0, 0])

print(ret)
