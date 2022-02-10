'''
>> P
9*9 판에서 스도쿠를 통해 빈칸을 채워 출력하라
    - 빈 칸은 '0'으로 표기
>> S
스도쿠 풀이 --> 맨 위부터 순서대로가 아니라 채울 수 있는 칸부터 채워감
1. 빈 칸 좌표를 저장
2. 빈 칸 좌표로 반복 탐색
3. 해당 좌표 가로/세로/3*3을 보며 채울 수 있는지 확인   
    - 채울 수 있다. -> 채우고 빈 칸 좌표에서 제거 
    - 못 채운다 -> 다른 칸으로 넘어가
4. 결과 출력

dfs 방식
첫 칸 부터 채워가는데 후보 (1~9중 3개가 없어) -> 3개로 반복 하는거야 그러다 아니면 쭉 올라와서 다른 수로 진행
    - 기저조건 -> board에 0이 없는가? -> return True해서 결과 출력 
다음 좌표로 어떻게 넘어가지? 
    - pop() & dfs() -> 탬색은 ran& append()
'''
# def dfs(cnt: int, x: int, y: int):
#     global empty, board
#     ret = False

#     if cnt == 0:
#         return True

#     # 1. 가로 / 세로 / 3*3을 요소를 모아서(중복없이) 그 중 없는 값으로 반복
#     # 2. empty에서 pop()해서 해당 좌표로 재귀호출 , cnt-1
#     # 3. 성공하면 기저로 달리는거고 실패하면 empty에 append()로 다시 추가
#     elem = set()
#     bx, by = x // 3, y // 3

#     for i in range(3):
#         for j in range(3):
#             elem.add(board[i + (3*bx)][j + (3*by)])  # 3*3
#             elem.add(board[j + (3*i)][y])  # 세로
#             elem.add(board[x][j + (3*i)])   # 가로

#     for v in [i for i in range(1, 10) if i not in elem]:
#         # for v in set(range(1, 10)) - elem:
#         (nx, ny) = empty.pop()
#         board[x][y] = v
#         ret = dfs(cnt-1, nx, ny)

#         if ret == True:
#             return True
#         else:
#             empty.append((nx, ny))
#             board[x][y] = 0

#     return False


# board = []
# empty = []
# for i in range(9):
#     row = list(map(int, input().split()))
#     board.append(row)
#     for j in range(len(row)):
#         if row[j] == 0:
#             empty.append((i, j))

# dfs(len(empty), empty[0][0], empty[0][1])
# for row in board:
#     print(*row)

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_promising(x, y):
    # promising = [i for i in range(1,10)]
    exist = set()
    bx, by = x // 3, y // 3  # x, y 값이 어느 블록에 있는지 확인(3*3 단위)

    for i in range(3):
        for j in range(3):
            exist.add(sudoku[x][j + (3*i)])  # 가로
            exist.add(sudoku[j + (3*i)][y])  # 세로
            exist.add(sudoku[i + (3*bx)][j + (3*by)])   # 3*3 block

    # 해당 칸 주위에 있는 값을 제외한 후보가 되는 값을 반환
    return [i for i in range(1, 10) if i not in exist]


flag = False  # 답 출력 여부 확인


def dfs(x):  # param = 빈 값(0)을 채운 개수
    global flag

    if flag:    # 답이 이미 출력됐다면
        return

    if x == len(zeros):  # 마지막 0까지 채워졌을 경우
        for row in sudoku:
            print(*row)
        flag = True
        return

    (i, j) = zeros[x]
    promising = is_promising(i, j)  # 검색할 숫자를 받음

    for num in promising:
        sudoku[i][j] = num
        dfs(x + 1)
        sudoku[i][j] = 0  # 초기화(정답이 아닌 경우)


dfs(0)
