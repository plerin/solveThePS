'''
> P

'''
MAX = 1000001
MOD = 1000000009

T = int(input())
nums = [int(input()) for _ in range(T)]

dp = [0] * MAX

# dp[1], dp[2] = 1, 2

for i in range(1, MAX):
    if i <= 2:
        dp[i] = i
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

for num in nums:
    print(dp[num])
