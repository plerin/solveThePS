'''
ai = 길이가 i인 수열에서 가장 긴 부분수열 최적해, k= i번째 값
ai = max(ai, aj + 1)  // a[0] ~ a[n] = 1 // 2중 반복 (1차(i)-수열 길이, 2차(j)-~i까지)
'''


def findLongDescSeq(n: int, seq: list):
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if seq[i] < seq[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


N = int(input())
seq = list(map(int, input().split()))

ret = findLongDescSeq(N, seq)

print(ret)
