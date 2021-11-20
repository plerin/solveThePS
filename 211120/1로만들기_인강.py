'''
> P
정수 x가 주어졌을 때 4가지 연산이 있다. 연산을 사용하여 1로 반드는 최소 값을 출력하라
    - if x % 5 == 0 then x // 5
    - if x % 3 == 0 then x // 3
    - if x % 2 == 0 then x // 2
    - x -= 1
> S
동적계획법
> L
ai = i를 1로 만드는 최적의 해(연산 최소 횟수)
ai = min(ai/5, ai/3, ai/2, ai-1) +1 , 단! i가 나누어 떨어질 때만 해당

접근
    - vari : dp(list) _ dp테이블

하향식(재귀)
    - param : x(int) _ 정수 x
    - vari : dp(global) 
    - logic
        1) base-condition : if x == 1 then return 0
        2) if dp[x] != 0 then return dp[x]
        3) dp[x] = dp[x-1] + 1  && if x % 5 == 0 dp[x] = min(dp[x]dp[x//5]) elif ...
    - return dp[x]
'''

# 하향식(top-down) - 재귀


def solve(x):
    if x == 1:
        return 0

    global dp

    if dp[x] != 0:
        return dp[x]

    # 재귀에서 dp[i] = solve(x-1) + 1 가 가장 위에 있으면 재귀 탈 때 계속 x-1을 먼저 구하므로 틀린다
    if x % 5 == 0:
        dp[x] = solve(x//5) + 1
    elif x % 3 == 0:
        dp[x] = solve(x//3) + 1
    elif x % 2 == 0:
        dp[x] = solve(x//2) + 1

    if dp[x] != 0:
        dp[x] = min(dp[x], solve(x-1) + 1)
    else:
        dp[x] = solve(x-1) + 1

    return dp[x]

# 상향식(bottom-up)


def solve2(x):
    dp = [0] * (x+1)

    for i in range(2, x+1):  # d[1] 은 0이니까!
        dp[i] = dp[i-1] + 1

        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5]+1)
        elif i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        elif i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)

    return dp[x]


X = int(input())

dp = [0] * (X+1)

ret = solve(X)
ret2 = solve2(X)

print(ret, ret2)
