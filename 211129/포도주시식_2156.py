'''
연속으로 3잔이상 마실 수 없다.
    => 이 때의 경우의 수를 구해서 점화식을 짜보자
'''
MAX = 10001


def solve(n: int, seq: list):
    if n <= 2:
        return sum(seq[:n])
    elif n == 3:
        return max(seq[0]+seq[1], seq[1]+seq[2], seq[0]+seq[2])

    dp = [0 for _ in range(n)]

    dp[0], dp[1] = seq[0], seq[0]+seq[1]
    dp[2] = max(seq[0]+seq[2], seq[1]+seq[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+seq[i-1]+seq[i], dp[i-2]+seq[i], dp[i-1])

    return max(dp)


n = int(input())
seq = [int(input()) for _ in range(n)]

ret = solve(n, seq)

print(ret)
