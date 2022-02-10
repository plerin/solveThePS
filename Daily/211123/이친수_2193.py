'''
> P
N이 주어졌을 때 N자리 이친수의 개수를 구하라
    - 0으로 시작하지 않는다
    - 1이 두 번 연속으로 나타나지 않은다
> S
동적 계획법

ai = ai-1 + ai-2, 단 a1=1, a2=1

오랜만에 
하향식(top-down)
    - dp테이블 = MAX(91) 크기로 0으로 초기화
    - param : n(int) _ 입력 값
    - vari : global dp 
    - logic
        1) 기저조건 : if n <= 2: then return 1
        2) if dp[n] != 0 then return dp[n]
        3) dp[n] = dp[n-1] + dp[n-2]
        4) return dp[n]

'''

MAX = 91


def topDown(n: int):
    global dp

    if n <= 2:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = topDown(n-1) + topDown(n-2)

    return dp[n]


N = int(input())

dp = [0] * MAX

ret = topDown(N)

print(ret)
