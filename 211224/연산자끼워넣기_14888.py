'''
>> P
N개의 수와 N-1개의 연산자를 이용한 식의 결과 중 가장 큰 값과 작은 값을 구하라
    - 사칙연산 우선순위 없이 앞에서 계산
    - 나눗셈 : 몫만 갖는다. 
    - 음수를 양수로 나눌 때 : 양수로 바꾼 뒤 몫을 취하고 그 값을 음수로 바꾼다.
>> S
모든 경우가 결과를 내고 그 결과 중 최소 / 최대 값을 갖는다
    - eval() 연산은 시간 소요가 크기 때문에 연산 그대로 사용하는 방법 사용

1. 순열(library)를 활용하는 방법
    1) minimum / maximum (int) 를 초기화 -1e9, 1e9
    2) 입력 받은 op_num을 부호 형태 리스트로 저장
    3) 함수 호출 -> purmutations를 구하고 반복
    4) 각 조합(case)마다 연산 수행 후 min/max 값 갱신
    5) 결과 출력

2. DFS를 활용하는 방법
    1) minimun / maximum 초기화
    2) op를 그대로 저장
    3) dfs 호출 param : depth(int), total(int), plus(int), minus(int), multiply(int), divide(int)
    4) if depth == N 인 경우 min/max 값 갱신
    5) if plus/minus/multiply/divied가 있는경우(True) depth+1, total+ 연산, 해당 연산 - 1
'''

from itertools import permutations
import sys

input = sys.stdin.readline


def use_library():
    global minimum, maximum

    for case in permutations(op, len(op)):
        total = num[0]
        for r in range(1, len(case)+1):
            if case[r-1] == '+':
                total += num[r]
            elif case[r-1] == '-':
                total -= num[r]
            elif case[r-1] == '*':
                total *= num[r]
            elif case[r-1] == '/':
                total = int(total / num[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total


def dfs(depth: int, total: int, plus: int, minus: int, multiply: int, divide: int):
    global minimum, maximum

    if depth == N:
        if minimum > total:
            minimum = total
        if maximum < total:
            maximum = total
        return

    if plus:
        dfs(depth+1, total + num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus, minus, multiply, divide-1)


N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for i, v in enumerate(op_num):
    for _ in range(v):
        op.append(op_list[i])

minimum = 1e9
maximum = -1e9

# use_library()
dfs(1, num[0], op_num[0], op_num[1], op_num[2], op_num[3])
print(maximum, minimum, sep='\n')


# def calculate(a: int, b: int, op: str):

#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         if a < 0:
#             return (a * (-1) // b) * (-1)
#         else:
#             return a // b


# def dfs(depth: int, result: int):
#     global visited, ans, min_v, max_v

#     if depth == N-1:
#         min_v = min(min_v, result)
#         max_v = max(max_v, result)
#         return

#     for i in range(N-1):
#         if not visited[i]:
#             visited[i] = True
#             cal_val = calculate(result, nums[depth+1], op[i])
#             dfs(depth+1, cal_val)
#             visited[i] = False


# N = int(input())
# nums = list(map(int, input().split()))
# visited = [False] * (N-1)
# # ans = set()
# min_v, max_v = int(1e9), -1

# op_list = list(map(int, input().split()))
# op_table = ['+', '-', '*', '/']
# op = []

# for i, v in enumerate(op_list):
#     for _ in range(v):
#         op.append(op_table[i])

# dfs(0, nums[0])

# print(max_v, min_v, sep='\n')
