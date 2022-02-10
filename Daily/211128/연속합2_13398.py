'''
수를 하나 제거할 수 있다(제거 안해도 됨)
    -> 이전 수를 제거하는 경우 & 현재 수를 제거하는 경우 
    -> 2차원 배열 -> [i][j] -> i = 순서, j[0] = 제거 없이 연속합 / j[1] = 제거하며 연속합 최적해
    -> a[i][0] = max(a[i][0], a[i-1][0]+ki) // a[i][1] = max(a[i-1][1] + ki, a[i-1][0])
'''


def solve(n: int, seq: list):
    dp = [[x for _ in range(2)] for x in seq]

    for i in range(1, n):
        dp[i][0] = max(dp[i][0], dp[i-1][0] + seq[i])
        dp[i][1] = max(dp[i-1][1] + seq[i], dp[i-1][0])

    maxv = -int(1e9)
    for i in range(n):
        maxv = max(maxv, max(dp[i]))
    return maxv


n = int(input())
seq = list(map(int, input().split()))

ret = solve(n, seq)

print(ret)
