'''

포도주는 3잔이상 연속 마실 수 없다.
포도주 한 잔이 추가되면 경우의 수는 2가지 마시거나 / 안마시거나

a[i][j] => i = i번째 잔 // j[0] = 안 마심, j[1] = 마심
    - i <= 2 -> 초기 갱신
    - i >= 3 ->
        [i][0] = [i-2][1] + [i-1][1]
        [i][1] = max([i-2][1] + now, [i-1][1] + now) # k = 현재 잔의 포도주 양
'''

MAX = 10001


# def solve(n: int, arr: int):
#     dp = [[0 for _ in range(2)] for _ in range(n+1)]

#     dp[1] = [0, arr[1]]
#     dp[2] = [arr[1], arr[1]+arr[2]]

#     for i in range(3, n+1):
#         dp[i][0] = dp[i-2][1] + dp[i-1][1]
#         dp[i][1] = max(dp[i-2][1] + arr[i], dp[i-1][0] + arr[i])

#     return max(dp[n])

def solve(n: int, arr: list):
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    dp[1] = [arr[1], arr[1], arr[1]]
    dp[2] = [arr[1]+arr[2], arr[2], arr[2]]

    for i in range(3, n+1):
        if i % 3 != 0:
            dp[i][0] = dp[i-2][0] + dp[i-1][0]
        if i % 3 != 1:
            dp[i][1] = dp[i-1][1] + arr[i]
            dp[i][2] = dp[i-2][2] + arr[i]


n = int(input())
amounts = [0] + [int(input()) for _ in range(n)]

ret = solve(n, amounts)

print(ret)
