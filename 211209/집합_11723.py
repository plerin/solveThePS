'''
> P
연산자와 숫자가 주어지면 해당 연산을 수행하고 check 연산일 때마다 결과 출력

M만큼 반복하며 연산자와 수를 받고
연산자에 따른 기능 처리 수행하는 함수 선언

집합을 비트마스크로 만들자 입력 값 범위가 20이니까 21로 하고 1~20수를 저장 어떻게?
    - 초기화 [0]
    - add : a | 1 << i 
    - remove : a = a & 1 << i
    - check : a >> i & 1
    - toggle : if check == 0 than add else remove
    - all : for i in range(1,21) remove
    - empty : for i in range(1,21) add

def operate(op:str, num:int):
    global arr

    if str == 'add':

'''
import sys

input = sys.stdin.readline


def operate(op: str, num: int):
    global ans

    if op == 'all':
        ans = (1 << 20) - 1
    elif op == 'empty':
        ans = 0
    elif op == 'add':
        ans = ans | (1 << num)
    elif op == 'remove':
        ans = ans & ~(1 << num)
    elif op == 'check':
        print(ans & (1 << num))
    elif op == 'toggle':
        ans = ans & ~(1 << num) if ans & (
            1 << num) else ans | (1 << num)
    # oper = input_val.split()


ans = 0

for _ in range(int(input())):
    # op, *num = input().split()
    oper = input().split()
    num = 0
    if oper[0] not in ('all', 'empty'):
        num = int(oper[1])

    operate(oper[0], num)
