# '''
# GOAL : N가지 종류의 동전으로 K만드는 경우의 수 반환

# 로직(전체 문제를 작은 부분문제의 합으로 바꿔라 & 그 과정에서 메모이제이션 수행)
#     1) 각 동전을 K값까지 반복하며 K를 만들 수 있는 경우 갱신
#     2)

# '''

# N, K = list(map(int, input().split()))
# coin = [int(input()) for _ in range(N)]


# dp = [0 for _ in range(K+1)]
# dp[0] = 1  # 동전 1개만 사용할 경우를 위함

# for i in coin:
#     for j in range(i, K+1):  # i가 3이면 1,2는 제외 _어짜피 0으로 초기화
#         if j-i >= 0:  # j값이 코인보다 같거나 크면 갱신하고 이전 값을 더해줌
#             # 이러면 코인크기부터 시작한다, 그리고 d[j-i]의 시작은 0이기에 코인 1개 사용하는 경우인 d[0]=1로 선언한 이유
#             dp[j] += dp[j-i]

# print(dp[K])


# 다시 풀기!

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for i in coin:
    for j in range(i, K+1):  # i가 3이면 1,2는 의미가 없기 때문에 i부터 시작
        if j-i >= 0:
            # dp[j] = dp[j]+dp[i-j] -> 이전 코인에서 구한 dp[j]에 현재 코인에서의 dp[i-j]를 합한 값을 dp[j]에 갱신
            dp[j] += dp[j-i]

print(dp[K])
