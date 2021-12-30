'''
>> P
N*N 체스판 위 퀸을 놓는 방법의 수를 구하라 
    - 퀸은 가로 / 세로 / 대각선 상에 놓일 수 없다
>> S
퀸을 놓는 경우를 1차원 배열에 저장해서 idx = 행 / val = 열 로 기록하자
    - 대각선 놓는 경우도 따로 계산 
    - dfs로 0행부터 N-1행까지 돌면서 안 놓인 곳에 퀸 놓고 체크(같은 열/대각선)
'''


def dfs(row: int):
    global board, ans

    if row == N:
        ans += 1
        return

    for i in range(N):
        if visited[i]:
            continue

        board[row] = i

        if check(row):
            visited[i] = True
            dfs(row+1)
            visited[i] = False


def check(n: int):
    for i in range(n):
        # 같은 열에 있거나 대각선 위에 있는 경우
        if board[i] == board[n] or (n-i == abs(board[n] - board[i])):
            return False

    return True


N = int(input())
board = [0] * N  # idx / val => 행 / 열
visited = [False] * N   # 퀸
ans = 0  # 경우의 수

dfs(0)

print(ans)
