'''
> P
정수 n을 1,2,3의 합으로 나타내는 방법의 수 구하기
    - 순서 상관 없음
> S
동적계획법

ai = ai-1 + ai-2 + ai-3 단, a1=1,a2=2,a3=3

dp = [0] * MAX(10)

상향식
    - param : n(int) _ 입력 값
    - dp 테이블 초기화 : if i <= 3 then return i && for i in range(4,MAX)

하향식
    - param : 동일
    - base-condition : if i <= 3 then return i

'''

MAX = 11


def bottomUp(n):
    global dp

    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, MAX):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


def topDown(n):
    global dp

    if n <= 3:
        return n if n <= 2 else 4

    if dp[n] != 0:
        return dp[n]

    dp[n] = topDown(n-1) + topDown(n-2) + topDown(n-3)

    return dp[n]


for _ in range(int(input())):
    n = int(input())

    dp = [0] * MAX

    ret = topDown(n)

    print(ret)
