'''

동적계획법 풀이
ai = i를 1,2,3으로 나타내는 방법의 수
d(i) = d(i-1) + d(i-2) + d(i-3) , d(1~3) 초기화 필요

브루트 포스

'''


def solve1(n: int):
    dp = [1 for _ in range(n+1)]

    for i in range(1, n+1):
        if i < 3:
            dp[i] = i
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    return dp[n]

# 하향식(top-down)


def solve2(n: int):
    if n == 3:
        return 4
    elif n < 3:
        return n

    global dp

    if dp[n] != 1:
        return dp[n]

    dp[n] = solve2(n-3) + solve2(n-2) + solve2(n-1)

    return dp[n]


for _ in range(int(input())):
    n = int(input())
    # ret = solve1(n)

    dp = [1 for i in range(n+1)]

    ret = solve2(n)
    print(ret)
