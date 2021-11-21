'''
> P
2*n 직사각형을 1*2, 2*1, 2*2 타일로 채우는 방법 구하라
> S
동적 계획법

2*1, 1*2 타일 사용 
점화식 : ai = ai-1 + ai-2 + (i-1) 단, a1 = 1, a2 = 2


'''

MAX = 1001


def solve(n):
    if n <= 2:
        return n

    global dp

    if dp[n] != 0:
        return dp[n]

    dp[n] = solve(n-1) + (solve(n-2) + 1)

    return dp[n]


n = int(input())

dp = [0] * MAX

ret = solve(n)

print(ret % 10007)
