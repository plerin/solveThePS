'''
> P
2*n 배열에서 사자를 배치하는 경우의 수를 구하라
    - 사자가 없는 경우도 포함
> S
동적 계획법

2차원 배열로 풀어보면
dp[i][j]
    - dp[i][0] = i줄에서 사자가 없는 겨웅
    - dp[i][1] = i줄에서 사자가 왼쪽에 있는 경우
    - dp[i][2] = i줄에서 사자가 오른쪽에 있는 경우

dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
dp[i][1] = dp[i-1][0] + dp[i-1][1]

'''

MOD = 9901

N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N+1)]

dp[1] = [1, 1, 1]

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

print(sum(dp[N]) % MOD)
