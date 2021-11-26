'''
> P
카드팩이 순서에 따라 카드가 들어있다. 
구매할 카드 개수(N)이 주어지면 지불해야하는 최대 금액 구하라
    - N개보다 많은 카드를 산 다음 카드를 버려서 만드는 것은 불가능하다
> S
동적 계획법

ai = i개 카드를 사는데 최적의 해, ki = i번째 카트팩 금액
점화식 -> ai = max(ai-k1, ai-k2, ..., ai-kn) 단, ai-k1 값은 초기화

dp = [0] 으로 MAX(1001) 초기화

상향식
    - param : packs(list) _ 카드팩 금액이 담긴 리스트
    - vari : global dp 
    - logic
        1) 2중 반복문 for price in packs then for i in range(price, MAX) if dp[i - price] != 0 (dp 값이 갱신 됐으면 그거 갖다 써) dp[i] = max(dp[i],dp[i-price]+price) 

'''

MAX = 1001  # 입력 값의 최대 값+1


def bottomUp(packs):
    global dp

    dp[0] = 0
    for pack in range(1, len(packs)+1):
        for i in range(pack, MAX):
            if dp[i - pack] != -1:
                dp[i] = max(dp[i], dp[i-pack] + packs[pack-1])

    return dp[N]


N = int(input())
packs = list(map(int, input().split()))

dp = [-1] * MAX

ret = bottomUp(packs)

print(ret)


# 카드 N개를 구매하는데 최대 값을 구하라

def bottomUp2(n: int, packs: list):
    global dp

    for i in range(1, n+1):
        for k in range(1, i+1):  # 1부터 i까지 반복을 하면서 이전 카드팩의 값을 채워줌
            if dp[i] == 0:
                dp[i] = dp[i-k] + packs[k]
            else:
                dp[i] = max(dp[i], dp[i-k] + packs[k])

    return dp[n]


N = int(input())
packs = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

ret = bottomUp2(N, packs)

print(ret)
