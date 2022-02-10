'''
> P
2*N 크기의 직사각형을 1*2, 2*1 타일로 채우는 방법을 구하라
    - 결과 값은 10007로 나눈 나머지로 출력
> S
동적계획법 활용
> L
ai = 2*i 직사각형을 채우는 최적의 해

점화식 -> ai = ai-1 + ai-2 단, a1 = 1, a2 = 2

풀이
dp = [0] * MAX(이 문제의 최대 값+1)

하향식
    - 기저조건 : if i <= 2 then return i
    - recursiveError 나면 rursive 제한 바꿔(default 1000) sys.setrecursionlimit(10**6)

    상향식
    - dp 초기화 : dp[1] = 1, dp[2] = 2 && 반복문은 range(3, max)

'''

import sys

MAX = 1001


def topDown(n):
    if n <= 2:
        return n

    global dp1

    if dp1[n] != 0:
        return dp1[n]

    dp1[n] = topDown(n-1) + topDown(n-2)

    return dp1[n]


def bottomUp(n):
    global dp2

    dp2[1], dp2[2] = 1, 2

    for i in range(3, n+1):
        dp2[i] = dp2[i-1] + dp2[i-2]

    return dp2[n]


n = int(input())

dp1 = [0] * MAX
dp2 = [0] * MAX

ret1 = topDown(n)
ret2 = bottomUp(n)

print(ret1 % 10007, ret2 % 10007)
