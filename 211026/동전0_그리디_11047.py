'''
[P]
N가지 종류 동전을 이용해 K원을 만드는 데 필요한 최소 개수
    - 동전 개수는 무한하다 가정
[S]
그리디(탐욕법) _ 최솟 값을 구하는데 있어 동전의 가치가 이전 가치보다 배수로 커져
    - 정당성 : 어떠한 경우에도 가치가 높은 동전을 사용해야 최소 개수를 사용함(최적의 해 성립) 
[L]
1. 입력 받기 
    1) N(int) _ 동전 종류, K(int) _ 목표 금액
    2) coins(list) _ 동전 리스트(가치에 따른 오름차순)
2. 함수 이용
    - PARAM : k(int) _ 목표 금액
    - LOGIC :
        1) declare cnt _ 동전 개수 담을 변수 선언
        1) loop with coins -> if coins[i] < K: then target = (k//coins[i]) * coins[i] -> cnt += k//coins[i] -> n = target
    - RETURN : cnt 
'''


def cntCoin(k):
    cnt = 0

    for coin in sorted(coins, reverse=True):
        if coin > k:
            continue

        target = (k // coin) * coin
        cnt += (k // coin)
        k -= target

    return cnt


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

ret = cntCoin(K)

print(ret)
