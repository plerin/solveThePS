'''
youtube url -> https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6&t=2555s

>> Keyword

>> P
N가지 종류의 화폐가 있고 개수를 최소한 이용해서 가치의 합이 M원이 되도록 함
M원을 만들기 위한 최소한의 화폐 개수를 구하라

>> S

접근
1. 문제 유형 구하기
완전 탐색, 그리디, 동적계획법이 떠오르는데 그리디는 안됨, 가장 좋은 해(최적해)만 선택했을 때 결과가 안나올 수 있어
2. 점화식 구하기
d(n) = min(d(n), d(n-k)+1), k = 현재 화폐값, dp는 화폐가치+1 크기로 만들고 값을 'inf'으로 초기화
3. 동적계획법 조건 확인
최적부분문제(큰 -> 작은 문제), 중복부분문제(같은 문제 반복)


코딩
1. 입력 값 받기 
n, m = map(int, input().split())
bill = [int(input()) for _ in range(n)]
2. dp 테이블 초기화
INF = float('inf')
dp = [INF] * 10001 # 범위가 1~10000
3. 함수 호출
print(efficient_compose(bill))
4. 함수 선언
def efficient_compose(bill: list) -> int:
    global dp
    
    for b in bill:
        dp[b] = 1
    
    for b in bill:
        for i in range(b, m+1, b):
            dp[i] = min(dp[i], dp[i-b]+1)
    
    return dp[m] if dp[m] != INF else -1
'''
INF = 10001  # 이 문제에서 최대 화폐 값이 10000이기 때문에 10001 == 만들 수 없는 수 == 무한 값


def efficient_compose(bill: list) -> int:
    global dp

    dp[0] = 0   # 0원을 만드는데 필요한 화폐는 0개
    for b in bill:
        for i in range(b, m+1):
            if dp[i-b] != INF:  # 현재 값(i)에서 현재 화폐(b) 뺀 값이 INF가 아니라면 == 이미 계산된 값이라면 갱신
                dp[i] = min(dp[i], dp[i-b]+1)

    return dp[m] if dp[m] != INF else -1


# 1. 입력 값 받기
n, m = map(int, input().split())
bill = [int(input()) for _ in range(n)]

dp = [INF] * 10001  # 범위가 1~10000

print(efficient_compose(bill))
