'''
>> P
N*N 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 방법 수를 구하라
    - 퀸 이동 반경 : 가로 / 세로 / 대각선
>> S
일차원 배열에 퀸 저장 _ idx : 행 / val : 열
    ex) board = [2,1,0] -> 0행 -> 2열, 1행 -> 1열, 2행 -> 0열
대각선 파악은 어떻게?
    - 열 - 열 == 행 - 행 이면 같은 대각선이라고 볼 수 있음
    - 현재 row를 입력 받고 열 / 대각선 판단 후 가능하면 True 아니면 False 반환
'''


def solve(depth: int):
    global visited, row, ans

    if depth == N:
        ans += 1
        return

    for i in range(N):
        if visisted[i]:  # 해당 열에 이미 퀸이 놓여있으면
            continue

        row[depth] = i

        if check(depth):
            visisted[i] = True
            solve(depth+1)
            visisted[i] = False


def check(n: int):
    for j in range(n):
        if row[n] == row[j] or n - j == abs(row[n] - row[j]):
            return False
    return True


N = int(input())
row = [0] * N
visisted = [False] * N
ans = 0

solve(0)

print(ans)
