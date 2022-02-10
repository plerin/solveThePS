'''
> P
수열의 크기(N)이 주어지고 n(n+1)/2 길이의 문자열이 주어진다.
- 부호 문자열에 맞는 수열을 찾아라

> S
1. 모든 숫자 체크할 변수 생성 _ check = [False] * 21( n + 10해주기 -> -10~10 -> 0 ~ 20)
    - 재귀함수로 사용하지 않은 숫자(if check == false)인 경우만 처리 아니면 continue
2. dfs 함수 선언
    - param : depth(int) _ 깊이(==N이면 판단시작), seq(list) _ 선택된 값들
    - vari : global N(int) _ 수열 갯수, global signs(list) _ 입력 부호
    - logic
        1) bc : depth == N then print
        2) for i in range(-10,11) -> idx = i+10 -> if check[idx] == True then continue
        3) seq.append(i)
        4) while seq: -> if ret_sign(sum(seq[:depth+1])) != sigh[depth] -> continue
        5)

sum() 값에 따라 부호 반환하는 함수
def ret_sign(seq_sum):
    if seq_sum > 0:
        return '+'
    elif seq_sum < 0:
        return '-':
    else:
        return '0'
'''
# from itertools import


def check(idx: int):
    hap = 0
    for i in range(idx, -1, -1):
        hap += ans[i]
        if hap == 0 and matrix[i][idx] != 0:
            return False
        elif hap > 0 and matrix[i][idx] <= 0:
            return False
        elif hap < 0 and matrix[i][idx] >= 0:
            return False
        return True


def solve(idx: int):
    global ans
    if idx == N:
        return True
    if matrix[idx][idx] == 0:
        ans[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        ans[idx] = matrix[idx][idx] * i
        if check(idx) and solve(idx+1):
            return True

    return False


N = int(input())
arr = list(map(str, input()))

matrix = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        sign = arr.pop(0)
        if sign == '+':
            matrix[i][j] = 1
        elif sign == '-':
            matrix[i][j] = -1

ans = [0] * N
solve(0)

print(' '.join(map(str, ans)))
