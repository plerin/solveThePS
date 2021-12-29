'''
>> P
R*C 보드가 대문자 알파벳으로 적혀있을 때 말이 움직일 수 있는 최대 칸 수
    - 말은 1행 1열에서 출발
    - 같은 알파벳을 두 번 지날 수 없다.
>> S
1. 알파벳을 숫자로 매칭해서 True/False 두고 이동할 때 그 알파벳이 False 인 경우만 이동
    - ord('A') = 65
2. 최대 값(ans)은 계속 갱신 따로 기저조건은 필요없어 알파벳으로 이동할 수 없으면 dfs 종료

vari
ans(int) = 0
visited(list) = [False] * 알파벳수(26)
move = [(-1,0),(1,0),(0,-1),(0,1)]

func
def dfs(cnt: int, x: int, y:int):
    global ans, visited
    
    ans = cnt if cnt > ans else ans

    for dx, dy in move:
        nx, ny = ss
        - check range & not visited
            update visited
            call dfs
            update visited
'''


def dfs2(cnt: int, x: int, y: int):
    global visited, ans

    ans = cnt if cnt > ans else ans

    for (dx, dy) in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C and not visited[ord(board[nx][ny])-65]:
            visited[ord(board[nx][ny])-65] = True
            dfs(cnt+1, nx, ny)
            visited[ord(board[nx][ny])-65] = False

    return


def dfs(cnt: int, x: int, y: int):
    global visited, ans

    ans = cnt if cnt > ans else ans

    for (dx, dy) in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visited:
            # visited[ord(board[nx][ny])-65] = True
            visited.add(board[nx][ny])
            dfs(cnt+1, nx, ny)
            visited.remove(board[nx][ny])
            # visited[ord(board[nx][ny])-65] = False

    return


R, C = map(int, input().split())
board = [input() for _ in range(R)]
# visited = [False] * 26
visited = set()
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0
print(board)
# visited[ord(board[0][0])-65] = True
visited.add(board[0][0])
dfs(1, 0, 0)

print(ans)
