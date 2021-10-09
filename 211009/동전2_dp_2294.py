'''
goal : n가지 동전을 사용하여 그 합이 k원이 되는 최소 개수 구하라
    1) 1<=n<=100, 1<=k<=10000)
    2) 불가능한 경우 -1 출력
1. 입력 받기
    1) N,K : 동전 종류와 목표 K원
    2) 동전 가치 : coin에 담아두자
2. 로직_dp
    0) 최적해 : ai = i를 조합하는데 사용되는 최소 동전 개수
    1) 부분 구분 구조로 변경 : min(각 동전 조합)
    2) 점화식 (ai:최적해, k: 동전): ai = min(ai,(ai-k)+1)
    3) dp 테이블 초기화 : [i] (i: k+1) , INF로 초기화  
'''

# 1
N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

# 2
dp = [10001] * (K+1)
dp[0] = 0

for i in coin:
    for j in range(i, K+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i]+1)


if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])
