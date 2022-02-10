'''
2*n 우리에 사자를 배치할 때 경우의 수
    - 사자는 가로/새로로 붙어있게 배치할 수 없다.
    - 사자를 배치하지 않는 경우도 있다

n-1 번째에 새로운 한 칸을 추가했을 때 나오는 경우의 수
위쪽에 배치 / 아래쪽에 배치 / 배치하지 않음 == 3가지
순서에 따라 위 3가지 경우를 모두 구해서 sum을 구한 값 == 최적해

[i][j] -> i = 순서 // j[0] = 위에 배치 & j[1] = 아래 배치 & j[2] = 배치 x

'''
MOD = 9901


def solve(n: int):
    dp = [[0 for _ in range(3)] for _ in range(n+1)]

    dp[1] = [1, 1, 1]

    for i in range(2, n+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD

    return sum(dp[n]) % MOD


N = int(input())

ret = solve(N)

print(ret)
