'''
>> P
N*N 체스판 위 퀸 N개를 서로 공격할 수 없도록 놓는 방법 수 구하라
    - 퀸은 가로/세로/대각선으로 공격가능
>> S
계속 의문이던 문제, 풀이를 봐도 이해가 안 가던 문제
간단하면서 어려워

행마다 퀸을 하나씩 놓고 가능하면 진행하다 끝에 도달했을 때(행이 N라인에) + 1 중간에 불가능 하면 return(백트래킹)
1. 0부터 N-1까지 재귀를 반복하며 끝에 도달했을 때(기저조건) + 1
2. board에 퀸이 저장된 좌표를 저장(1차원) idx = 행 / val = 열 
3. 인덱스마다 진행하니 행이 겹칠 일은 없으니 열과 대각선 체크
    - 열 : row[a] == row[b]
    - 대각선 : 행 - 행 == 열 - 열이 같으면 같은 대각선 위에 있다.

'''


def solve(row: int):
    global visited, ans

    if row == N:
        ans += 1
        return

    for i in range(N):
        if visited[i]:  # 해당 열에 이미 퀸이 놓여진 경우
            continue

        board[row] = i  # row행 i열에 퀸을 놓는다

        if check(row):  # 퀸의 위치가 적절한지 판단
            visited[i] = True
            solve(row+1)
            visited[i] = False


def check(n: int):
    for i in range(n):
        # 행끼리의 차 == 열끼리 차의 절대값이 같으면 대각선 상에 있는 것임
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False

    return True


# N = int(input())
# board = [0] * N
# visited = [False] * N
# ans = 0

# solve(0)

# print(ans)
def solve2(n: int):
    global board, ans

    if n == N:
        ans += 1
        return

    for i in range(N):
        board[n] = i
        if check(n):
            solve2(n+1)
        # for j in range(n):
        #     if board[j] == board[n] or (n - j == abs(board[n] - board[j])):
        #         break
        #     else:
        #         solve2(n+1)


N = int(input())
board = [0] * N
ans = 0

solve2(0)

print(ans)
