'''

ai = i개 집을 칠하는 비용의 최솟 값(최적해)
집을 칠하는 경우의 수는 색상 선택 하는 경우  R / G / B == 3가지
a[i][j] => i = 순서 // j = 색상(R/G/B)
a[i][0] = min(a[i-1][1], a[i-1][2]) + seq[i][0] ....

여기서 추가할 조건 하나 1번과 n번이 붙어있다(서로 같은 색상을 칠해선 안된다)
첫 번째에서 [0](r)을 고르면 마지막은 [1][2] 중 최솟 값을 선택 이를 반복

'''
import sys

input = sys.stdin.readline
MAX = int(1e9)


def solve(num: int, cost: list):
    dp = [[0 for _ in range(3)] for _ in range(num)]

    ans = MAX
    for i in range(3):
        dp[0] = [MAX, MAX, MAX]
        dp[0][i] = cost[0][i]

        for j in range(1, num):
            dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
            dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
            dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]

        for k in range(3):
            if k == i:
                continue
            ans = min(ans, dp[num-1][k])

    return ans


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

ret = solve(N, cost)

print(ret)
