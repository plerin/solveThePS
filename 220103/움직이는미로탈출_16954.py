'''
>> P
8*8 체스판에서 왼쪽 가장 아래 칸에서 오른족 가장 위칸으로 이동할 때 가능 여부 파악
    - 출발점 : (7,0) // 도착점 : (0,7)
    - 캐릭터는 인접모든 칸으로 이동 가능(대각선포함) + 가만히 있을 수 있음
    - 캐릭터 이동 후 벽이동 ==> 벽이 캐릭터 있는 칸으로 오면 실패(return 0)
>> S
1. 방향벡터로 이동가능한 모든 경우를 추가 총 10가지(가만히 있는것까지)
2. 벽이 아래 칸으로 움직임 (더이상 칸이 없다면 없어짐)
    - 캐릭터 움직임 반복문 끝나고
    - 벽이 [x+1][y] 으로 움직이는데 x+1이 N이면 '.' -> global로 하고 계속 바뀜


'''

from collections import deque
import sys

SIZE = 8
START = (7, 0)
END = (0, 7)


def escape_maze(x: int, y: int):
    global maze, wall
    # 최단 거리는 구하는 것도 아니고 maze에서 벽의 위치가 바뀌니까 또다른 변수는 필요 없음
    # 아니 그래도 방문여부 체크는 해야지 안그럼 안나아가
    queue = deque([(x, y)])
    # visit[x][y] = True

    while queue:
        visit = [[False] * SIZE for _ in range(SIZE)]
        x, y = queue.popleft()

        if x == END[0] and y == END[1]:
            return 1
        # 사람 이동
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if dx == 0 and dy == 0:
                queue.append((nx, ny))

            if 0 <= nx < SIZE and 0 <= ny < SIZE and not visit[nx][ny] and maze[nx][ny] != '#':
                visit[nx][ny] = True
                queue.append((nx, ny))

        # 벽이동
        new_wall = []
        for wx, wy in wall:
            wx, wy = wx + 1, wy    # 아래로 한 칸 이동

            maze[wx-1][wy] = '.'
            # 더이상 갈 곳이 없을 때
            if wx == SIZE:
                continue
            # 사람 만났을 때
            if (wx, wy) in queue:
                queue.remove((wx, wy))
            # 빈 칸일 때
            maze[wx][wy] = '#'
            new_wall.append((wx, wy))

        wall = new_wall
        print(wall)
    return 0


# maze = [list(input().rstrip()) for _ in range(SIZE)]
maze = []
wall = []
for i in range(SIZE):
    row = list(input().rstrip())
    maze.append(row)
    for j in range(SIZE):
        if row[j] == '#':
            wall.append((i, j))

move = [(-1, -1), (-1, 1), (-1, 0), (1, -1),
        (1, 1), (1, 0), (0, -1), (0, 1), (0, 0)]

ans = escape_maze(START[0], START[1])

print(ans)
