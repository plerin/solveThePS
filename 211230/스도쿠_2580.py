'''
>> P
9*9 스도쿠 판에에서 모든 빈 칸이 채워진 모습 출력하라
>> S
1. 빈칸인 좌표를 구한다.
2. 빈칸인 좌표로 dfs를 호출
    - cnt가 빈칸의 개수와 같아질 때까지 -> 같아지면 fl 
    - 전역함수로 flag를 false로 만들고 채워지면 flag -> true dfs 빠져나오기
    - empty[cnt]로 다음 빈칸을 찾아 
    - 가로/세로/3*3 블록에 없는 수를 받아와서(함수) 그걸 반복

>> F
1. 알아서 구하기
2. 
flag = Flase
def dfs(cnt: int):
    global board
    if flag:
        return
    if cnt == len(empty):
        flag = True
        return
    
    (x, y) = empty[cnt]
    candidate = check(x, y)

    for c in candidate:
        board[x][y] = c
        dfs(cnt+1)
        board[x][y] = 0
'''


def check(x: int, y: int):
    exist = set()
    bx, by = x // 3, y // 3
    for i in range(3):
        for j in range(3):
            exist.add(board[x][j+(3*i)])    # column
            exist.add(board[j+(3*i)][y])    # row
            exist.add(board[i + (3*bx)][j + (3*by)])    # 3*3 block

    return set(range(1, 10)) - exist


def dfs(cnt: int):
    global board, flag

    if flag:
        return

    if cnt == len(zero):
        flag = True
        for row in board:
            print(*row)
        return

    (x, y) = zero[cnt]
    candidate = check(x, y)

    for c in candidate:
        print(c)
        board[x][y] = c
        dfs(cnt+1)
        board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
flag = False

dfs(0)
