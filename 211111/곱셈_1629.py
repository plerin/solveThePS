'''
>P
a를 b번 곱한 수를 c로 나눈 값을 출력
>S
재귀로 풀어보자
>L
a와 나눈 횟수(cnt)를 인자로 주고 횟수가 b번이 되면 c로 나눈 값을 출력하고 리턴 
'''


# def multiple(a, b, c):
#     ans = 1
#     for _ in range(b):
#         ans = ans * a % c

#     return ans


# A, B, C = map(int, input().split())

# ret = multiple(A, B, C)

# print(ret)

'''
지수 법칙 // 나눗셈 법칙을 사용하여 
'''


import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# 지수법칙 & 나머지 분배 법칙을 통해 풀이함


def multi(b: int):
    if b == 1:
        return a % c

    tmp = multi(b//2)
    if b % 2 == 0:
        return (tmp * tmp) % c
    else:
        return (tmp * tmp * a) % c


# 이진수로 풀이 _ a를 b만큼 곱할 때
def func2(a: int, b: int):
    ans = 1
    while b:
        if b % 2 == 1:
            ans = ans * a % c
        a = a*a % c  # a는 반복할 수록 a승만큼 커짐
        b //= 2  # b는 반복할 수록 2씩 나눠진다

    return ans


print(multi(b))
print(func2(a, b))
