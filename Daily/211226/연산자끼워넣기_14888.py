'''
>> P
N개의 수열과 N-1개인 연산자가 주어졌을 때 연산자의 조합으로 만들 수 있는 최대/최소 값을 구하라
    - 수열의 순서는 바꾸면 안된다
    - 연산자는 + / - / * / // 순서를 갖는 숫자 4개로 주어진다(구분자 : ' ')
>> S
dfs 풀이로 진행
    - 각 연산마다 수행하는 경우로 파라미터와 로직 설정
    - a연산을 수행하면 depth+1, total+연산, a연산-1

def def(depth: int, total: int, plus: int, minus: int, multiple: int, divide: int)
    - vari: global maximum/minimum(int) 최대/최소 값 갱신
    - logic
        1) if depth == N -> update min/max & return
        2) if plus / miuus / multiple / divide -> call using by recursive
'''
from itertools import permutations


def use_library(num: int):  # 모든 순열 경우의 수를 구하면 시간 초과
    global minimum, maximum

    for case in permutations(op, num-1):
        total = seq[0]

        for i in range(len(case)):
            if case[i] == '+':
                total += seq[i+1]
            elif case[i] == '-':
                total -= seq[i+1]
            elif case[i] == '*':
                total *= seq[i+1]
            elif case[i] == '/':
                total = int(total / seq[i+1])

        if minimum > total:
            minimum = total
        if maximum < total:
            maximum = total


def dfs(depth: int, total: int, plus: int, minus: int, multiple: int, divide: int):
    global minimum, maximum

    if depth == N:
        if minimum > total:
            minimum = total
        if maximum < total:
            maximum = total
        return

    if plus:
        dfs(depth+1, total+seq[depth], plus-1, minus, multiple, divide)
    if minus:
        dfs(depth+1, total-seq[depth], plus, minus-1, multiple, divide)
    if multiple:
        dfs(depth+1, total*seq[depth], plus, minus, multiple-1, divide)
    if divide:
        dfs(depth+1, int(total/seq[depth]), plus, minus, multiple, divide-1)


N = int(input())
seq = list(map(int, input().split()))
op_list = list(map(int, input().split()))
op_table = ['+', '-', '*', '/']
op = []

for idx, cnt in enumerate(op_list):
    for i in range(cnt):
        op.append(op_table[idx])


minimum, maximum = 1e9, -1e9

dfs(1, seq[0], op[0], op[1], op[2], op[3])
# use_library(N)
print(maximum, minimum, sep='\n')
