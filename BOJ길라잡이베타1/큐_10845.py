'''
>P
스택을 기능을 구현하라
>S
구현문제
명령에 따라 처리
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque([])

for _ in range(N):
    cmd = input()
    ret = -1
    if cmd.startswith("push"):
        queue.append(int(cmd.split()[1]))
    elif cmd.startswith("pop"):
        ret = queue.popleft() if len(queue) != 0 else -1
        print(ret)
    elif cmd.startswith("size"):
        print(len(queue))
    elif cmd.startswith("empty"):
        ret = 1 if len(queue) == 0 else 0
        print(ret)
    elif cmd.startswith("front"):
        ret = queue[0] if len(queue) != 0 else -1
        print(ret)
    elif cmd.startswith("back"):
        ret = queue[-1] if len(queue) != 0 else -1
        print(ret)
