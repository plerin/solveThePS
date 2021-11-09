'''
> P
1~n까지의 수를 스택에 넣어 뽑아 수열을 만든다.
    - push = '+' // pop = '-' // 불가능한 경우 'NO'를 출력
    - PUSH 순서는 오름차순
> S
구현 _ 스택
입력 수열에 따라 스택 구현
수열 모든 요소마다  '+' / '-' / 'NO' 를 판단해야 함
> L
1. 입력 받기
    - n(int) : 수열 수 // seq(list) : 수열 값 담는 리스트
2. 로직
    - 변수 : arr(list) _ 1~n까지 담는 리스트 // stack(list) : 스택 활용위한 리스트
    - 로직
        1) for i in seq _ seq 반복하며 하나씩 사용
        2) i 뽑기 위해서 arr에서 stack 으로 push 하고 pop _ 이 과정에서 print
        3) 만약 i와 pop()한 수가 다르면 no 출력
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque([i for i in range(1, n+1)])
seq = [int(input()) for _ in range(n)]
stack = []
ret = []
for i in seq:
    while not stack or stack[-1] != i:
        if not arr:
            print('NO')
            exit()
        stack.append(arr.popleft())
        ret.append('+')

    stack.pop()
    ret.append('-')

print(*ret, sep='\n')
