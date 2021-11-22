'''

'''
import sys

sys.setrecursionlimit(10*6)

MAX = 1001


def topDown(n):
    if n <= 1:
        return n
    elif n == 2:
        return 3

    global dp

    if dp[n] != 0:
        return dp[n]

    dp[n] = topDown(n-1) + topDown(n-2) * 2

    return dp[n]


def bottomUp(n):
    global dp

    dp[1], dp[2] = 1, 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    return dp[n]


n = int(input())

dp = [0] * MAX

ret = bottomUp(n)

print(ret % 10007)
