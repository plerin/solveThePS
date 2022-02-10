'''
> P
괄호의 짝이 맞으면 yes 틀리면 no를 반환하라
> S
구현 _ 스택 활용 문제 
접근
    1. (이면 STACK에 넣고
    2. )이면 스택에서 빼 
    -> (가 없는데 )가 들어오거나 모두 입력 받았는데 (가 남아있으면 NO
'''

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    stack = []
    arr = list(map(str, input().rstrip()))
    ret = 0

    for c in arr:
        if c == '(':
            ret += 1
        else:
            ret -= 1

        if ret < 0:
            break

    if ret == 0:
        print('YES')
    else:
        print('NO')
