'''

점화식
a[i][j] => i = 길이(세로)   // j[3] = [사자x / 사자 왼 / 사자 오] 
a[i][j] = a[i-1][0] + a[i-1][1] + a[i-1][2], 단 a[1] = [1, 1, 1]
설명들어간다 a[1] = [1,1,1] 2*1 우리에서 사자 없는 경우(1) / 사자가 왼쪽에 있는경우(1) / 사자가 오른쪽에 있는 경우(1)
'''

MAX = 100001
MOD = 9901


def bottomUp(n: int):
    dp = [[0 for _ in range(3)] for _ in range(MAX)]

    dp[1] = [1, 1, 1]

    for i in range(2, MAX):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD

    return sum(dp[n]) % MOD


N = int(input())

ret = bottomUp(N)

print(ret)
