'''
> P
x를 3가지 연산을 사용해서 1로만드는 최소 횟수를 출력하라
    - if x % 3 == 0 then x // 3
    - if x % 2 == 0 then x // 2
    - x -= 1

> S
그리디 / 동적계획법 -> 그리디가 안되는 경우는 1,2번 조건이 있고 무조건 3으로 나누는게 1을 만드는 가장 최적의 방법이 아님

> L

ai = i를 1로 만드는 최적의 해(최소 연산 횟수)
점화식 -> ai = min(ai/3, ai/2, ai-1) + 1 단, 나누어 떨어질 때만 나누기

dp
    - MAX으로 초기화, 크기는 1000001 or X+1

하향식(top-down)
    - param : x(int) _ 입력 값
    - vari : dp(global)
    - logic 
        1) 기저조건 : if x == 1 then return 0
        2) if dp[x] != 0 then return dp[x]
        3) if i % 3 == 0 then dp[x] = dp[x//3]+1 and 2
        4) dp[x] = min(dp[x], dp[x-1]+1)
    - return dp[x]

상향식(bottom-up)

'''
MAX = 1000001


def solve(x):
    global dp

    if x == 1:
        return 0

    if dp[x] != MAX:
        return dp[x]

    if x % 3 == 0:
        dp[x] = solve(x//3)+1
    elif x % 2 == 0:
        dp[x] = solve(x//2)+1

    dp[x] = min(dp[x], solve(x-1)+1)

    return dp[x]


def solve2(x):
    global dp

    dp[1] = 0

    for i in range(2, x+1):
        dp[i] = dp[i-1] + 1

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)

    return dp[x]


X = int(input())

dp = [X+1] * (X+1)  # 여기서 MAX값으로 초기화 할 필요는 없다

ret = solve2(X)

print(ret)
