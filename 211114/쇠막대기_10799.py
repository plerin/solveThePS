'''
> P
여러 개의 쇠막대기를 레이저로 절단하려고 한다, 쇠막대기를 아래에서 위로 겹쳐 놓고 레이저로 수직 발사하여 절단하려고 했을 때 조각의 총 개수
    - 쇠막대기는 자신보다 긴 막대기 위에만 놓을 수 있다. (끝점은 겹치지 않음)
    - 레이저는 막대기마다 최소 1개
    - 레이저는 막대기 끝점과 겹치지 않늗나)
> S
접근
    1. ()가 채워지는 과정을 idx +/-로 표현
    2. (를 만날 때마다 idx+=1 그러다가 if meet '()' then ret+=idx  // elif meet ')' then ret+=1 
    3. '()'를 만찾는 과정은 len(s)-1만큼 반복하며 i와 i+1를 사용  i와 i+1이 ()이 아니라면 계속 진행 ()맞으면 idx += 2 
'''

import sys

input = sys.stdin.readline

s = list(map(str, input().rstrip()))
idx = 0
stack = 0
ret = 0

while idx < len(s)-1:
    now, nex = s[idx], s[idx+1]
    idx += 1
    if now == '(' and nex == ')':
        idx += 1
        ret += stack
        pass
    elif now == '(':
        stack += 1
        pass
    elif now == ')':
        stack -= 1
        ret += 1
        pass
print(stack)
print(ret)
