'''
[P]
가로, 세로가 N인 지도에서 집이 연결된 단지를 수하여 단지의 속하는 집의 수를 오름차순으로 출력

[S]
그래프 탐색_연결 요소(Connected Component)유형 
    - BFS / DFS로 풀이
[L]
1. 지도 입력 받기
    - N(int)을 통해 map(이차원배열) 입력 받기
2. 변수 선언
    - dx/dy : 방향벡터 _ 상하좌우 이동위함
    - ret(int) : 단지 별 집의 수를 담아 결과 출력 위함
3. 지도를 탐색하며 함수 호출
    - 모든 좌표에서 함수 호출하여 단지여부 확인 & 단지 수 리턴
4. 함수 선언(dfs)
    - PARAM : coord(tuple) _ 현재 x,y좌표
    - LOGIC :
        1) 기저조건 : '1'이 아니라면 return 0
        2) 방향벡터를 반복하며 '범위(N*N)에 속한다면 CNT+=1 하며 재귀호출
    - RETURN : cnt(int) _ 집의 개수 반환
5. 결과 출력
    - 오름차순으로 출력
'''
# 4


def findGroup(coord):
    cnt = 1
    x, y = coord[0], coord[1]

    graph[x][y] = 0

    for i in range(len(dx)):
        nx, ny = x+dx[i], y+dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            cnt += findGroup((nx, ny))
    return cnt


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ret = []

# 3
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            ret.append(findGroup((i, j)))

# 5
print(len(ret), *sorted(ret), sep='\n')
