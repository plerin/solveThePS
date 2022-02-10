'''
>> P
10*10 보드에서 100번째 칸을 가는데 걸리는 최소 횟수 구하라
    - 1에서 출발 100에 도착
    - 사다리와 뱀의 수가 주어진다.(단방향)
    - 주사위를 내가 원하는 값으로 조작이 가능함!
>> S
그래프에서 최소 횟수를 구하라 => BFS
    - deque 사용 _ from collections import deque
    - 방문처리필요
    - 
뱀의 수가 왜 주어졌을까? 그냥 사다리만 타고 가면 되잖아??
    - 사다리 타고 2-> 50 , 뱀타고 51-> 48, 사다리타고 49-> 99 갈 수 도 있어 적절하게 조합해야함.

전략
1차원(x) 전장에서 1에서 100을 가는 최소 값을 찾는 것
    - 지름길과 낭떨어지가 주어짐
1. 1~6범위 안에 사다리가 없으면 6만 가
    - 아니면 해당 사다리 또는 뱀으로 가
2. 1번을 반복하기 

코딩
이동 방법
move_lots = False
for i in range(6):
    if pos + i in arr:
        move_lots = True
        queue.append((pos+i, cnt+1))
if move_lots == False:
    dfs(pos+6, cnt+1)




전략
1. 출발은 1 도착은 100(1차원) 그리고 주사위를 굴리면 무조건 앞으로 간다
    - 1에서 6을 가는 동안 경우 처리
        1) 100에 도착하는 경우 -> 값 갱신하고 함수 리턴
        2) trick(사다리/뱀)타고 이동하는 경우 -> 해당 칸의 값으로 queue에 입력
        3) 1,2 둘다 아닌 경우 -> 6더한 값만 queue에 입력
'''

from collections import deque, defaultdict
import heapq

SIZE = 101


# def bfs(pos: int):
#     global board

#     queue = deque([pos])
#     board[pos] = 0

#     while queue:
#         pos = queue.popleft()

#         for i in range(1, 7):
#             n_pos = pos + i
#             if 0 <= n_pos <= 100 and board[n_pos] == -1:

#                 if n_pos in trick.keys():
#                     n_pos = trick[n_pos]
#                 if board[n_pos] == -1:
#                     board[n_pos] = board[pos] + 1
#                     queue.append(n_pos)


# N, M = map(int, input().split())
# board = [-1] * SIZE

# trick = defaultdict(int)
# for i in range(N+M):
#     x, y = map(int, input().split())
#     trick[x] = y

# bfs(1)

# print(board[100])


# def bfs(pos: int, cnt: int):
#     global board, ans

#     queue = deque([pos])
#     board[pos] = 0

#     while queue:
#         pos = queue.popleft()
#         next_pos, cnt = 0, board[pos]+1
#         for i in range(1, 7):
#             next_pos = pos+i
#             if pos + i == 100:
#                 ans = min(ans, cnt)
#                 break
#             if next_pos in trick.keys():
#                 move_trick = trick[next_pos]

#                 board[move_trick] = cnt
#                 queue.append(move_trick)
#         # if use_trick == False:
#             if i == 6:
#                 queue.append(next_pos)
#                 board[next_pos] = cnt


def bfs(pos: int, cnt: int):
    global board, ans

    queue = []
    heapq.heappush(queue, (cnt, pos))

    while queue:
        cnt, pos = heapq.heappop(queue)

        for i in range(1, 7):
            next_pos, next_cnt = pos+i, cnt+1
            if next_pos == 100:
                ans = next_cnt
                return
            if 0 <= next_pos <= 100:
                if next_pos in trick.keys():
                    next_pos = trick[next_pos]
                    # heapq.heappush(queue, (next_cnt, move_trick))
                heapq.heappush(queue, (next_cnt, next_pos))


N, M = map(int, input().split())
board = [-1] * SIZE
trick = defaultdict(int)

for _ in range(N+M):
    x, y = map(int, input().split())
    trick[x] = y

ans = 1e9
bfs(1, 0)
print(ans)
