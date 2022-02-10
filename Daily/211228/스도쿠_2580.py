'''
>> P
9*9 가 주어질 때 스토쿠를 채운 뒤 최종 모습 출려가
    - 빈칸은 0으로 주어진다
    - row별로 1~9까지 그리고 3*3 정사각형안에도 1~9까지 수가 중복없이 쓰여진다.
>> S
1. 0인 곳을 탐색하며 채워넣을 수 있는 경우 먼저 채운다
    - row에 하나만 비어있는 경우
        - 가로 : [고정][i] // 세로 : [i][고정] 
    - 3*3안에 하나만 비어있는 경우
        - 행/열 모두 /3하면 어느 block인지 구할 수 있어 해당 block탐색
    - while로 계속 돌기
        - 0인 것이 없을 때까지

값이 0인 좌표를 리스트로 저장하고 
'''
from collections import deque


def check(x: int, y: int):
    global board
    # print(board[x])
    row = set(board[x])
    col = set([board[i][y] for i in range(9)])

    if len(row) == 9:
        val = [i for i in range(1, 10) if i not in row]
        board[x][y] = val[0]
        return True

    if len(col) == 9:
        val = [i for i in range(1, 10) if i not in col]
        board[x][y] = val[0]
        return True

    bx = x // 3
    by = y // 3
    pack = set()
    # o~2에 bx를 곱해
    for i in range(3):
        for j in range(3):
            pack.add(board[i+(3*bx)][j+(3*by)])

    if len(pack) == 9:
        val = [i for i in range(1, 10) if i not in pack]
        board[x][y] = val[0]
        return True
    return False
    #     board[0]
    # for i in range(9):
    #     board[x][i]


# board = [list(map(int, input().split())) for _ in range(9)]
board = []
empty = deque([])
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(len(row)):
        if row[j] == 0:
            empty.append((i, j))
# print(board[0])
# print(set(board[0]))
while empty:
    (x, y) = empty.popleft()
    if check(x, y):
        continue
    empty.append((x, y))

for row in board:
    print(*row)
# print(*board)
