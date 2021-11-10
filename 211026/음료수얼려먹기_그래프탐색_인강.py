'''
[P]
N*M 크기의 얼음 틀에 생성되는 총 아이스크림 개수 구하라
    - 0 : 뚤린 부분 / 1 : 칸막이 존재
    - 상, 하, 좌, 우 붙어있는 경우 연결된 것으로 간주
[S]
그래프 탐색(Graph-Search) -> BFS/DFS 풀이
    - N*M을 그래프로 보고 연결된 지점을 방문 처리
[L]
0. 변수 선언
    - N(int), M(int) : 행과 열
    - step(list) : tuple 형태로 구성된 방향벡터
    - ret(int) : 
1. N*M(이차배열)를 0으로 초기화 _ 개수는 +1(인덱스 0은 사용 안함)
2. 이중 반복문으로 모든 요소에 접근 -> 값이 '0'이면 그래프 탐색 처리
3. 함수 선언
    - PARAM : (x,y) _ 현재 좌표
    - LOGIC
        0) 해당 좌표 값이 '1'이면 return False
        1) 방문 처리 _ [x][y] = 1
        2) 방향벡터 이용하며 연결 노드 방문 -> N*M을 넘었거나 값이 '1'이면 처리(continue) // 아니면 dfs() 호출
        3) return True
'''


def dfs(x, y):
    if graph[x][y] == 1:
        return False

    graph[x][y] = 1

    for step in steps:
        nx, ny = x+step[0], y+step[1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        dfs(nx, ny)

    return True


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ret = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            ret += 1

print(ret)
