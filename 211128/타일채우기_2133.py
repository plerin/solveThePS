'''
ai = 3*i 벽을 2*1, 1*2 타일로 채우는 경우의 수 
짝수인 경우만 채울 수 있다.

dp[4] = dp[2] + dp[2] + 2
dp[6] = dp[2] + dp[4] + 2

for i in range(1,n+1//2):
    dp[(i+1)*2] = dp[2] + dp[i*2] + 2
'''
MAX = 31


def solve(n: int):
    dp = [0 for i in range(MAX)]
    dp[2] = 3

    for i in range(4, MAX):
        if i % 2 != 0:
            continue
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

    return dp[n]


N = int(input())

ret = solve(N)

print(ret)
