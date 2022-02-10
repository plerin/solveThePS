'''

0~n 정수에서 k개를 더해 그 합이 n이 되는 경우를 구하라
    - n과 k의 관계가 예사롭지 않아 어떤 관계가 있을까?

n의 값과 상관없이 k=1 이라면 결과는 1(자기자신)
k의 값과 상관없이 n=1 이라면 결과는 k(0과 1 조합)

그리고 n과 k 상관관계를 찾아서 나온 점화식
d[i][j] = d[i-1][j] + d[i][j-1], 단 d[1][n] = n, d[n][1] = 1

'''
MAX = 201
MOD = 1000000000


def solve(num: int, cnt: int):
    dp = [[0 for _ in range(MAX)] for _ in range(MAX)]

    for i in range(1, MAX):
        dp[1][i] = i
        dp[i][1] = 1

    for i in range(2, MAX):
        for j in range(2, MAX):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[num][cnt] % MOD


N, K = map(int, input().split())

ret = solve(N, K)

print(ret)
