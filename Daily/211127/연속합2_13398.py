
def solve(n: int, seq: list):
    dp = [[seq[i] for _ in range(3)] for i in range(n)]
    # for i in range(n):
    #     dp[i][0] = seq[i]

    dp[1][0] = max(dp[1][0], dp[0][0] + seq[1])
    dp[1][2] = max(dp[1][2], dp[0][1] + seq[1])

    maxv = max(dp[0][1], dp[0][0])
    maxv = max(maxv, dp[0][1], dp[0][0])

    for i in range(2, n):
        dp[i][0] = max(dp[i][0], dp[i-1][0] + seq[i])
        dp[i][1] = max(dp[i][1], dp[i-2][0] + seq[i])
        dp[i][2] = max(dp[i][2], dp[i-1][1] + seq[i])

        maxv = max(maxv, dp[i][0], dp[i][2])

    return maxv


n = int(input())
seq = list(map(int, input().split()))

ret = solve(n, seq)

print(ret)
#
