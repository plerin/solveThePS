'''

> S
1. 시간과 메모리 제한이 촉박 -> 효율적인 방법 찾아야 함
    - 비트 마스크 사용
        -> 함수 만들고 입력 연산에 따른 처리 수행
'''

import sys

input = sys.stdin.readline


def operate(op: str, num: int):
    global ans

    if op == 'add':
        ans |= (1 << num)
    elif op == 'remove':
        ans &= ~(1 << num)
    elif op == 'check':
        print((ans >> num) & 1)
    elif op == 'toggle':
        ans = ans & ~(1 << num) if ans & (1 << num) else ans | (1 << num)
        pass
    elif op == 'all':
        ans = (1 << 21) - 1
    elif op == 'empty':
        ans = 0

    print(op, num)
    pass


ans = 0

for _ in range(int(input())):
    op, *num = input().split()

    print(op, num)

    operate(op, int(num[0]) if num else 0)
