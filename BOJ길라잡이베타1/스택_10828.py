'''
>P
스택을 기능을 구현하라
>S
구현문제
명령에 따라 처리
'''
import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    cmd = input()
    ret = -1
    if cmd.startswith("push"):
        stack.append(int(cmd.split()[1]))
    elif cmd.startswith("pop"):
        ret = stack.pop() if len(stack) != 0 else -1
        print(ret)
    elif cmd.startswith("size"):
        print(len(stack))
    elif cmd.startswith("empty"):
        ret = 1 if len(stack) == 0 else 0
        print(ret)
    elif cmd.startswith("top"):
        ret = stack[-1] if len(stack) != 0 else -1
        print(ret)
