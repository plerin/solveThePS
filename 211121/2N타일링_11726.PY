'''
> P
2*n 크기의 직사각형을 1*2, 2*1 타일로 채우는 경우 출력

> S
동적 계획법

ai = 2*i 직사각형을 채우는 최적의 해
ai = max(ai-3+3,ai-4+5) , a1=1, a2 = 2, a3 = 3 

MAX = 1001
dp = [0] * MAX

하향식
    - param : n(int) _ 입력 값
    - vari : dp(list) _ dp테이블
    - logic
        1) 기저조건 : if x in (1,2,3) return 1,2,3
        2) if dp[x] != 0 then return
        3) dp[x] = (dp[x-3]+3, dp[x-4]+5)
'''

MAX = 1001

# 점화식이 ai = ai-2 + ai-1 이라면


def solve(n):
    global dp

    if n <= 2:
        return n

    if dp[n] != 0:
        return dp[n]

    dp[n] = solve(n-2) + solve(n-1)

    return dp[n]


n = int(input())

dp = [0] * MAX

ret = solve(n)

print(ret % 10007)
