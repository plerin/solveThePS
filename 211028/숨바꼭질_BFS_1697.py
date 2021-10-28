'''
[P]
수빈이는 N에 동생은 K지점에 있을 때 수빈이가 동생을 찾는 가장 빠른 시간을 구하라
    - 수빈이가 X일 때 X-1 / X+1 / 2X 로만 이동할 수 있다.
[S]
가장 빠른 시간 == 그래프 탐색 중 BFS로 풀어볼 것이다.
    - 1차원 배열위에서 방문 처리하며 방향 벡터로 인접 노드 탐색
[L]
1. BFS 준비물
    - 라이브러리 추가 _ deque, sys(입력)
    - 그래프(graph) _ 1차원 배열
    - 방향벡터(dx) _ 이동 가능 범위 _ [-1,1,2]
2. 입력 받기
    - N(int), K(int) _ 수민, 동생 위치
3. 함수 선언
    - 목적 : bfs 로직 수행
    - param : v _ 출발노드
    - logic
        1) deque에 담고 반복 실행 
        2) 방향 벡터로 이동하며 범위를 벗어나지 않고(0<=x<1000000) '0'이면 비용 값 갱신(=[x][y]+1)
        3) K 만나면 함수 종료
4. 결과 출력
'''

from collections import deque
import sys

input = sys.stdin.readline

MAX_V = 100001


def findSister(v):
    queue = deque([v])

    while queue:
        x = queue.popleft()

        for mv in dx:
            nx = eval(str(x)+mv)

            if 0 <= nx < MAX_V and graph[nx] == 0:
                graph[nx] = graph[x]+1
                queue.append(nx)
                if nx == K:
                    return


N, K = map(int, input().split())
graph = [0] * MAX_V
dx = ['-1', '+1', '*2']

graph[N] = 1

findSister(N)

print(graph[K]-1)
