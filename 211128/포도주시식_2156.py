
def solve(n: int, seq: list):
    dp = [0 for _ in range(n)]

    dp[0] = seq[0]
    dp[1] = seq[0] + seq[1]
    dp[2] = max(seq[0]+seq[2], seq[1]+seq[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + seq[i-1] + seq[i], dp[i-2] + seq[i], dp[i-1])

    return max(dp)


n = int(input())
juice = [int(input()) for _ in range(n)]

ret = solve(n, juice)

print(ret)
