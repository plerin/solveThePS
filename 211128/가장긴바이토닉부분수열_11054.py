'''
바이토닉 수열 = 왼->오 가면서 커지고 특정 수 기준으로 오->왼 가면서 작아지는 수열

ai = i길이 수열에서 바이토닉 부분 수열 중 최대 길이 값(최적해)
[i][j] -> i = 순서 // j[0] = -> 증가 부분 수열 길이 최적해, j[1] = <- 증가 부분 수열 길이 최적해
초기화는 1로(방향 상관없기 기본 값 1)

maxv = 0
maxv = max(maxv, max(dp[i]))

'''
import copy


def solve(n: int, seq: list):
    dp = [[1 for _ in range(2)] for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i][0] = max(dp[i][0], dp[i-1][0]+1)

    seq_rev = copy.deepcopy(seq)
    seq_rev.reverse()
    # for k in range(n-1,(n-1)-i,-1):
    #     if seq[(n-1)-i] > seq[k]:
    #         dp[i][1] = max()
    for i in range(n):
        for j in range(i):
            if seq_rev[i] > seq_rev[j]:
                # dp[i][1] = max(dp[i][1], dp[i-1][1]+1)
                dp[(n-1)-i][1] = max(dp[(n-1)-i][1], dp[(n-1)-(i-1)][1] + 1)

    maxv = 0
    for i in range(n):
        maxv = max(maxv, max(dp[i]))

    print(dp)
    return maxv


N = int(input())
seq = list(map(int, input().split()))

ret = solve(N, seq)

print(ret)
