'''
[P]
강호는 면접보러 가야한다. F층 건물에서 G층에 가기 위해 S층에서 버튼을 최소 몇 번 눌러야 하는가 
    - U : U층 위로 올라 감 // D : D층 아래로 내려 감
    - 도달할 수 없다면 'use the stairs' 출력
[S]
1차원 배열에서 특정 조건에 해당하는 위치로 이동하며 최단 경로 찾는 문제 
    - 1차원 배열 = 그래프 & 최단 경로로 접근하는 BFS 풀이 
[L]
1. BFS 준비물
    - 라이브러리 _ heapq, sys
    - graph _ 최댓 값 크기(1000000)크기 만큼 만들고 [0]으로 채워놓기(층별 버튼 횟수 저장)
    - 방향벡터 _ U, D에 해당하는 수로 만들기
2. 입력 받기
    - F, S, G, U, D : 모두 INT형 _ F층 건물 S층 시작 G층 목표 U층 위로 D층 아래로
3. 함수 선언
    - 목표 : BFS 로직 수행하여 목표 층(G)에 해당하는 횟수 저장
    - PARAM : s(int) _ 출발 층
    - LOGIC :  
        1) queue(deque)에 s를 담고 반복문 수행
        2) 방향벡터로 다음 층 구해서 다음과 같은 조건 체크
            - 건물 층에 해당 여부(1<=x<=MAX) & graph[x] == 0
        3) 2번 조건에 해당하면 graph 갱신하고 큐에 담아
    - RETURN : 없음
4. 결과 출력
    - graph에서 해당 층(G) 값이 0이 아니면 출력 0이면 'use the stairs"출력
'''

from collections import deque
import sys

input = sys.stdin.readline


def howManyPushButton(s):
    queue = deque([s])
    while queue:
        floor = queue.popleft()

        for i in range(len(dx)):
            if i == 0:
                next_f = floor + dx[i]
            else:
                next_f = floor - dx[i]

            if 0 <= next_f < (F+1) and graph[next_f] == 0:
                graph[next_f] = graph[floor]+1
                queue.append(next_f)
                if next_f == G:
                    return


F, S, G, U, D = map(int, input().split())
graph = [0] * (F+1)
dx = [U, D]

graph[S] = 1

# if S == G:
#     print(0)
#     exit()

howManyPushButton(S)

if graph[G] == 0:
    print("use the stairs")
else:
    print(graph[G]-1)
