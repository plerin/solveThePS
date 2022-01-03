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


>> 느낀점
풀이는 전형적인 방법이라도 리소스(시간/메모리) 조건을 맞추기가 어렵다.
1. 시간초과가 나올 때 방법 2가지
    1) import sys 사용하여 input()을 최적화
    2) pypy3로 제출
    3) in(O(n)) int -> str(casting)과 같은 연산을 최적화하는 방법 찾기
    4) list()보다 set() 만약 메모리 에러가 난다면 list(MAX) = FALSE 로 만들어놓고 사용
2. 문제를 보며 조급해하지말자
한 문제만 풀어도 되니까 조급하지말고 안 풀릴 수록 차가워져야해
인생에 대부분의 문제는 정답이 없는 경우가 많다!
'''

from collections import deque
import sys

input = sys.stdin.readline

MAX = 10000  # 0~9999


def solve(num: int, op: str):
    global register

    queue = deque([(num, op)])
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
