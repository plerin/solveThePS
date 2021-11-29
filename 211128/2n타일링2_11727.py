'''

타일이 새로 추가 됐을 때 경우의 수
1 => 2*1 
2 -> 1*2 & 2*2 (2가지 타일로 채울 수 있다.)
3 부터는 1과 2의 경우의 중복
ai = ai-1 + ai-2 * 2, a1 = 1, a2 = 3
'''

MOD = 10007


def fillTile(n: int):
    if n == 1:
        return 1

    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 1, 3

    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2] * 2) % MOD

    return dp[n-1]


n = int(input())

ret = fillTile(n)

print(ret)
