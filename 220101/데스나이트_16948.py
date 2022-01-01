'''
>> P
체스에서 새로운 말을 만들었다. 이 말이 (r2,c2)까지 이동하는 최소 이동 횟수 구하라

>> S
체스판에서 말의 이동 최소 횟수 
    -> 전형적인 BFS 문제

>> 전략
1. 이동 가능 경우를 방향벡터로 만들어 놓음
2. 해당 범위에 포함될 경우 기존 값 +1로 해서 queue에 담아
3. 이동 좌표가 (r2,c2)면 종료
4. 정답 출력

'''

from collections import deque


def bfs(x: int, y: int):
    global board

    queue = deque([(x, y)])
    board[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for (dx, dy) in move:
            nx = x + dx
            ny = y + dy

            if nx == r2 and ny == c2:
                board[nx][ny] = board[x][y] + 1
                return

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[-1] * N for _ in range(N)]
move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

bfs(r1, c1)

# print(board)
print(board[r2][c2])
