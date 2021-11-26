
def solve(n, arr: list):
    dp = [[0 for _ in range(2)] for _ in range(n)]

    dp[0] = [arr[0], arr[0]]

    for i in range(1, n):
        if dp[i-1][1] < arr[i]:
            dp[i][0] = dp[i-1][0] + arr[i]
            dp[i][1] = arr[i]
        else:
            dp[i] = [arr[i], arr[i]]


N = int(input())
A = list(map(int, input().split()))

ret = solve(N, A)

print(ret)
