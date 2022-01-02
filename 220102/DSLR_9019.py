'''
>> P
D, S, L, R 명령만 이용가능한 계산기에서 입력된 숫자 A를 B로 만드는 최소 명령어를 나열하라
    - 여러가지만 아무거나 출력
    - D : 2배 만약 9999보다 크다면 10000으로 나눈 나머지를 저장
    - S : -1, 만약 N이 0이라면 9999 저장
    - L : 왼쪽으로 회전
    - R : 오른족으로 회전
>> S
연산을 수행해서 최소 경우를 구하라 -> 그리디 / BFS / 동적계획법
    - 그리디는 안됨 : 어느 연산이 가장 우선되는 것이 없어
    - BFS : 가능할 듯 보여
    - 4가지 경우로 나누면 되니까 가능하지 않을까?
>> 전략
4가지 연산을 수행하며 처음 만나는 숫자인 경우만 갱신
    - 9999를 max값으로 하여 False로 초기화하고 모든 경우(연산 결과)가 False면 누적 연산으로 갱신
    - 연산을 수행하며 B를 만나면 함수 종료 후 결과 출력
각 연산을 어떻게 처리하느냐?
    - QUEUE에서 POPLEFT한 값으로(시작은 A)로 4번 반복문을 돌며 각 연산을 수행하고 처음 보는 값인 경우만(false) 처리
'''

from collections import deque
import sys

input = sys.stdin.readline

MAX = 10000  # 0~9999


def solve(num: int, op: str):
    global register

    # visited = set()
    queue = deque([(num, op)])
    # visited.add(num)
    register[num] = True

    while queue:
        num, op = queue.popleft()

        if num == B:
            print(op)
            return

        for o in ['D', 'S', 'L', 'R']:
            n_num = cal(num, o)

            if register[n_num]:
                continue
            # register[n_num] = register[num] + o
            register[n_num] = True
            queue.append((n_num, op+o))


def cal(num: int, op: str):
    # op로 num을 연산 후 리턴한다
    if op == 'D':
        return (num * 2) % 10000
    elif op == 'S':
        return num - 1 if num != 0 else 9999
    elif op == 'L':
        front = num % 1000
        back = num // 1000
        # s, r = divmod(num, 1000)
        return front * 10 + back
    elif op == 'R':
        front = num % 10
        back = num // 10
        # s, r = divmod(num, 10)
        return front * 1000 + back


if __name__ == '__main__':

    for _ in range(int(input())):
        A, B = map(int, input().split())

        register = [False] * MAX

        solve(A, '')

        # print(register[B])
