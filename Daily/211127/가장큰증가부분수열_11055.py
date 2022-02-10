'''

ai = 길이가 i인 수열에서 부분 증가 합이 가장 큰 최적해, k = 수열 i번째 값
ai = max(ai, aj+k) _ 0 ~ i-1까지 반복 & ai = ki 값으로 초기화

'''


def findIncreMax(n: int, seq: list):
    dp = [x for x in seq]

    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j]+seq[i])

    return max(dp)


N = int(input())
seq = list(map(int, input().split()))

ret = findIncreMax(N, seq)

print(ret)
