'''
>> P
8*8 체스판 위 (7,0) -> (0,7)로 이동 할 수 있는 여부 구하기
    - 0 : 빈 칸 // 1 : 벽
    - 벽은 매초마다 1칸씩 아래로 움직인다 _ (x, y) -> (x+1, y)
    - 이동범위 : 상하좌우 + 대각선 + 제자리 = 9가지
    - 캐릭터가 이동 후 벽이 움직인다.
>> S
비용을 구할 필요가 없다.  & 맨위에 도착하면 됨(어짜피 벽이 1칸씩 내려고이 때문!)
    -> nx가 0에 도달하면 종료(return 1)
다음 칸으로 이동하는 칸이 벽이 아니고 벽이 내려올 칸이 아니면 된다.
    - 벽이면 그 곳으로 이동할 수 없음
    - 움직인 후 그 자리에 벽이 오면 그것도 이동 불가한 자리
        -> [nx][ny] != '#' and [nx-1][ny] != '#'

벽의 움직임
wall 좌표를 구해놓고 pop() 하고 x+1 값이 넘위를 넘으면 continue 아니면 append(x+1,y)

다시 생각해보기 
몇 초가 지나갔는지 기록을 해주면 ? -> turn이라고 하자
turn == 1 -> 나는 (7,0) -> (7,1)이동할 때 (nx(7),1)과 (nx-turn(7-1),1)이  '#'(벽)이 아니면 추가
이걸 다시 풀어보자 내 현재 위치는 (x,y) 이동할 위치를(nx,ny)라고 했을 때
if arr[nx-turn][ny] != '#' and arr[nx-turn-1][ny] != '#'라면 queue.append((nx,ny,dist))
    -> dist == 7 -> return 1 7턴동안 벽은 모두 사라졌을테니까
    -> deque([(7, 0, 0)])


'''

from collections import deque


def isin(x: int, y: int):
    if -1 < x < 8 and -1 < y < 8:
        return True
    return False


def solve():
    queue = deque([(7, 0, 0)])  # 출발 (x,y), 흐른 시간(초)
    visited = [[False for _ in range(8)] for _ in range(8)] # 재방문 방지
    visited[7][0] = True

    while queue:
        x, y, time = queue.popleft()

        if time == 7:   # 7초가 흐르면 벽은 모두 사라져있어서 도착지(0.7)에 갈 수 있음
            return 1

        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if not isin(nx, ny):
                continue

            # 움직일 좌표(nx)에서 흐른 시간(time)을 뺀 값에 벽('#')이 없다면 queue에 담아
            if board[nx-time][ny] != '#' and board[nx-time-1][ny] != '#':
                if not visited[nx][ny] or dx == 0 and dy == 0:  # 멈춰있는 경우 포함
                    queue.append((nx, ny, time+1))
                    visited[nx][ny] = True

    return 0


board = [list(input()) for _ in range(8)]
move = [(-1, -1), (-1, 1), (-1, 0), (0, -1),
        (0, 1), (0, 0), (1, -1), (1, 1), (1, 0)]

ans = solve()

print(ans)
