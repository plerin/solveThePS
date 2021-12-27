'''
>> P
N*M 보드와 4개의 버튼으로 이루어진 게임, 보드 위 동전 2개가 있을 때 하나만 떨어뜨리기 위한 최소 경우(버튼 클릭) 구하라
    - 4개 버튼은 상/하/좌/우 로 구성
>> S
동전은 같이 이동하고 둘 중 한개만 떨어뜨려야 함
    - 카운트를 할까 이동하고 몇개가 범위 밖으로 나가는지
    - 그리고 10회가 넘어가도 return False
정리하자
1. 2차원 배열로 받을건데 '.'은 0으로 '#'는 1로 매칭
2. 방향벡터로 움직일 때마다 매칭되는 동전 2개를 매칭으로 저장해(nx,ny)가 아니라 (nx1,ny2,nx2,ny2) 그리고 같이 이동해 어떤 방향이든 

def dfs(cnt:int, x1,y1,x2,y2)
    - vari : visited(set) _ 방문할 때마다 (x1~y2)까지 tuple형식으로 저장, ret = False
    - bc#1 : if cnt > 10 -> return ret
    - logic
        1) for (dx, dy) in move:
            nx1 ~ ny2 update & 
    - return ret
    
'''


def dfs(depth: int, x1: int, y1: int, x2: int, y2: int):
    global board, ans

    if depth > 10:  # 기저 조건
        return

    for (dx, dy) in move:
        nx1, ny1 = x1 + dx, y1 + dy
        nx2, ny2 = x2 + dx, y2 + dy
        cnt = 0
        # 3가지 경우 #라서 제자리 / .라서 이동 / 범위 밖이라 사라지는 경우
        if not (0 <= nx1 < N and 0 <= ny1 < M):
            cnt += 1
        if not (0 <= nx2 < N and 0 <= ny2 < M):
            cnt += 1

        if cnt == 1:    # 동전 2개 중 하나만 빠져나갔을 때
            ans = min(ans, depth)
            continue

        if cnt == 2:
            continue

        if board[nx1][ny1] == '#':  # 벽이면 자리 그대로
            nx1, ny1 = x1, y1
        if board[nx2][ny2] == '#':  # 벽이면 자리 그대로
            nx2, ny2 = x2, y2

        if not (nx1, ny1, nx2, ny2) in visited:  # 방문 체크 안되있으면
            visited.add((nx1, ny1, nx2, ny2))
            dfs(depth+1, nx1, ny1, nx2, ny2)
            visited.remove((nx1, ny1, nx2, ny2))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()  # 좌표 2개를 확인하기 위해 (x1,y1,x2,y2)로 방문 체크
x1, y1, x2, y2 = -1, -1, -1, -1
ans = 1e9

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            board[i][j] = '.'
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j

visited.add((x1, y1, x2, y2))
dfs(1, x1, y1, x2, y2)

print(ans if ans != 1e9 else -1)
