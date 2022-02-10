'''
> P 
수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열의 길이를 구하라
> S
동적 계획법 _ 동적 계획법이 아니여도 풀 수 있을 것 같은데 이게 더 빠른가?

ai = 크기가 i인 수열의 최적해(가장 긴 부분수열 길이)
dp -> 현재 값이 이전 값 보다 큰 경우 증가해야하기 때문에 2차원 배열로 나타나낼 것 
    -> dp[i][0] = i까지 수열의 부분 수열 길이   dp[i][1] = i까지 수열의 마지막 값(다음 값과 비교하기위해)
    -> dp[i] = [dp[i-1][0]+1, s] if s(현재 값) > dp[i-1][1] else [dp[i-1][0], dp[i-1][1]]
        단, dp[1] = [1, seq[0]]
'''


def bottomUp(n: int, seq: list):
    global dp

    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j]+1)


N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N

bottomUp(N, seq)
print(max(dp))  # 가장 긴 부분수열이 꼭 dp 맨 뒤이지 않을 수 있따!
