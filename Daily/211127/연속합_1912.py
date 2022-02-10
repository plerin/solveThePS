

n = int(input())
seq = list(map(int, input().split()))

dp = [x for x in seq]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+seq[i])  # 현재 값
print(dp)
print(max(dp))
