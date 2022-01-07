'''
>> P
동전 N 종류의 합으로 K원을 만드려고 할 때 필요한 동전의 최솟값을 구하라
>> S
종류가 다양하고 높은 가치의 동전을 사용할 수록 최소 개수를 사용함
    -> 그리디 알고리즘

전략
1. 동전을 입력받고(가치는 오름차순)
2. pop()하며 해당 동전의 가치에서 뽑을 수 있는 개수를 구하며 진행
3. 동전 개수 반환

함수
def get_coinnum():
    global coin, ans
    while coin:
        c = coin.pop()
        if c > K:
            continue
        s, r = divmod(K, c)
        ans += s
        K = r
'''


def get_coin():
    global coin, ans, K

    while coin:
        c = coin.pop()

        if c > K:
            continue

        s, r = divmod(K, c)
        K = r
        ans += s


N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
ans = 0

get_coin()

print(ans)
