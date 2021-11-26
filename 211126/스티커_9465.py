'''

ai = 2*i 스티커 배열에서 얻을 수 있는 최대 점수(최적해)
i가 커질 때 선택할 수 있는 경우는 2가지
    - i-1의 최대 값을 선택하는 것
    - i-2의 최대 값에 현재 최대 값을 선택하는 것
ai = max(ai-1, ai-2 + k) , k = i번째의 최대 값
'''


# def solve(n: int, sticker: list):
#     dp = [0] * (n+1)

#     dp[1] = max(sticker[0][0], sticker[1][0])
#     dp[2] = max(sticker[0][0] + sticker[1][1], sticker[1][0] + sticker[0][1])

#     for i in range(3, n+1):
#         dp[i] = max(dp[i-1]+min(sticker[0][i-1], sticker[1][i-1]),
#                     dp[i-2]+max(sticker[0][i-1], sticker[1][i-1]))
#     print(dp)
#     return dp[n]

def solve(n: int, arr: list):
    # dp = [[0 for _ in range(3)] for _ in range(n+1)]
    global dp

    dp[1] = [0, arr[0][0], arr[1][0]]

    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2])+arr[0][i-1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])+arr[1][i-1]

    return max(dp[i])


for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    ret = solve(n, arr)
    print(ret)
