'''
> P
2*n 직사각형을 1*2, 2*1, 2*2 타일로 채우는 방법 구하라
> S
동적 계획법

ai = 2*i 에서 타일로 채우는 최적의 해(방법의 수)
ai = ai-1 + (ai-2) * 2, 단 a1 =  


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
