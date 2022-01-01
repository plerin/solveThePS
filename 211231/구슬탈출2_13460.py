'''
>> P
N*M 보드가 있고 빨간 구슬/ 파란 구슬/ 구멍/ 빈 칸/ 장애물이 있을 때
구슬을 굴려서 빨간 구슬만 구멍으로 빼내는데 소요되는 최소 횟수 구하라
    - 상/하/좌/우로 구슬이 움직이지 않을때까지 이동
    - 10번 이하로 빼낼 수 없다면 -1 출력
>> S
상하좌우 이동시 벽을 만날 때까지
    - board[x][y] == '#' 이면 중지 // 'B/R'이면 한 칸 나아가며 -1 // '.'이면 한 칸 나아가며 + 1
    -> R/B 모두 이동한 뒤 해당 좌표가 False면 dfs 재귀 True면 continue
좌표를 모두 False로 초기화하고 해당 좌표를 방문할 때마다 True로 바꿔놓을까?
    - visited[1 << 9][1 << 9][1 << 9][1 << 9] = False # [rx][ry][bx][by]
'''


def dfs(depth: int, rx: int, ry: int, bx: int, by: int):
    global ans, flag

    if flag:
        return

    if depth > 9:
        flag = True
        return

    # 4방향 장애물 나올 때까지 이동
    for dx, dy in move:
        move_r = 0
        move_b = 0
        goal_r = False
        goal_b = False
        # 함수호출해서 r/b 각각 다음 좌표랑 구멍 들어간 여부 리턴
        # 구멍 r만 들어갔으면 종료
        #
        while board[rx][ry] != '#':
            rx = rx + dx
            ry = rx + dy
            if board[rx][ry] in ('R', 'B'):
                continue
            if board[rx][ry] == 'O':
                goal_r = True
            move_r += 1

        while board[bx][by] != '#':
            bx = bx + dx
            by = bx + dy
            if board[bx][by] in ('R', 'B'):
                continue
            if board[bx][by] == 'O':
                goal_b = True
            move_b += 1

        if (rx+(dx*move_r), ry+(dx*move_r), bx+(dx*move_b), by+(dx*move_b)) not in visited:
            dfs(depth+1, rx+(dx*move_r), ry+(dx*move_r),
                bx+(dx*move_b), by+(dx*move_b))
        # while rx

    # red, blue 좌표가 기존에 있었던 곳이면 pass 아니면 재귀 호출


N, M = map(int, input().split())
board = []
visited = set()
red, blue = (), ()
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 / 하 / 좌 / 우

for i in range(N):
    row = input()
    board.append(row)
    for j in range(len(row)):
        if row[j] == 'R':
            red = (i, j)
        if row[j] == 'B':
            blue = (i, j)

ans = 1e9
flag = False    # ans 값 구했을 때
visited.add((red[0], red[1], blue[0], blue[1]))
dfs(0, red[0], red[1], blue[0], blue[1])

print(ans)
# print(red, blue)
