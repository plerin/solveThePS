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
    for pack in range(1, len(packs)+1):
        for i in range(pack, MAX):
            if dp[i - pack] != INF:
                dp[i] = min(dp[i], dp[i - pack] + packs[pack-1])

    return dp[n]


N = int(input())
packs = list(map(int, input().split()))
dp = [INF] * MAX

ret = bottomUp(N, packs)

print(ret)
