'''

그리디 알고리즘

>> Concept

현재 상황에서 가장 좋은 선택만 하는 것
아이디어를 떠올릴 수 있는 능력 요구
정당성 분석이 중요 -> 가장 좋은 것을 선택했을 때 최적의 해를 구할 수 있는지 여부 검증

>> P
계산을 도와줘야 한다
거스름돈으로 500원, 100원, 50원, 10원 동전이 무한히 존재할 때 
N원을 거슬러 줘야할 최소 개수를 구하시오

>> 아이디어
가장 높은 가치 동전부터 주면 되겠다.

>> 정당성 분석
큰 단위가 항상 작은 단위의 배수 -> 작은 동전들의 종합으로 다른 해가 나올 수 없어

'''

n = 1260

coin = [500, 100, 50, 10]
ans = 0
idx = 0

while n:
    ans += n//coin[idx]
    n %= coin[idx]

    idx += 1

print(ans)
