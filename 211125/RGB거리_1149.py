'''
> P
1~N 개에 걸쳐 R,G,B 비용이 주어졌다 모든 집을 친하는 최솟 값을 구하라

aij = i번 집의 r(j=0) / g(j=1) / b(j=2) 의 최적해

a[i][0] = max(a[i-1][1], a[i-1][2]) + a[i][0]
a[i][1] = max(a[i-1][0], a[i-1][2]) + a[i][1]
a[i][2] = max(a[i-1][0], a[i-1][1]) + a[i][2]
단, dp는 입력 값으로 초기화

출력 : min(dp[n])

상향식
    - param : n(int), seq(list)
    - vari : global dp
    - logic
        1) 
'''


def bottomUp(n: int):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0] = costs[0]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    return min(dp[n-1])


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

ret = bottomUp(N)

print(ret)
