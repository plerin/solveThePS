'''

a[i][j] => i = 수의 길이 // j = 맨 뒤자리가 0~9일 때 경우의 수
a[i][j] = a[i-1][0~j]의 합
    ex) a[3][3] = a[2][0] + a[2][1] + a[2][2] + a[2][3] (이래야 뒤에 3이 들어갈 수 있으니까)
'''

MAX = 1001
MOD = 10007


def bottomUp(n: int):
    dp = [[0 for _ in range(10)] for _ in range(MAX)]

    for i in range(10):
        dp[1][i] = 1

    for i in range(2, MAX):
        for j in range(10):
            for k in range(j+1):
                dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

    return sum(dp[n]) % MOD


N = int(input())

ret = bottomUp(N)

print(ret)
