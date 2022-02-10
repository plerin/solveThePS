'''
> P 
카드팩 i는 i개의 카드를 포함하고 있다.
n개의 카드를 구매하는데 가장 저렴한 방법을 출력하라 
> S
동적계획법

ai = i개 카드를 구매하는 최적의 해(최소 금액), i = 카드 팩 수 ki = 카드팩 i의 금액
점화식 = ai = min(ai-1 + k1, ai-2 + k2, ... , ai-n + kn)

dp -> INF(int(1e9)) 으로 사이즈 1001 만큼 초기화 

상향식(bottom-up)
    - param : N(int) _ 구매할 카드의 수
    - vari : dp(list) _ dp 테이블   //  
    - logic
        1) dp[0] = 0 으로 초기화
        2) 화폐를 반복하며 최저 값으로 갱신 
'''

MAX = 1001
INF = int(1e9)


def bottomUp(n: int, packs: list):
    global dp

    dp[0] = 0
    for pack in range(1, len(packs)+1):  # 카드팩 종류 만큼
        for i in range(pack, MAX):  # 카드팩의 카드 수 부터 MAX까지
            if dp[i - pack] != INF:  # i - pack dp 값을 이전에 갱신한 적이 있다면
                dp[i] = min(dp[i], dp[i - pack] + packs[pack-1])

    return dp[n]


N = int(input())
packs = list(map(int, input().split()))
dp = [INF] * MAX

ret = bottomUp(N, packs)

print(ret)

# 풀이 2 더 간결한 방법
N = int(input())

packs = [0] + list(map(int, input().split()))
dp = [False] * (N+1)

for i in range(1, N+1):  # 카드팩 종류만큼 반복
    for k in range(1, i+1):  # 1부터 현재 카드 개수 만큼
        if dp[i] == False:  # 처음 만나면 값 갱신
            dp[i] = dp[i-k] + packs[k]
        else:   # 기존에 있는 값이면 그 중 min 값으로 갱신
            dp[i] = min(dp[i], dp[i-k]+packs[k])
print(dp[N])
