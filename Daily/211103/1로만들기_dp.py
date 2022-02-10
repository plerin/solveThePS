'''
[P]
정수 X가 주어졌을 때 정해진 연산을 사용해서 1로 만드는 최소 값 구하라
    1. 5로 나누어 떨어지면 나누기 5
    2. 3으로 나누어 떨어지면 나누기 3
    3. 2로 나누어 떨어지면 나누기 2 
    4. 1 빼기
[S]
4가지 연산으로 1을 만들어야 함
    - 그리디는 아니야 -> 최적의 경우를 먼저 골라야 하는데 무조건 5로 나눈다고 빠르지 않아 5/3/2 나누는 경우가 모두 호환되지 않아
    - DP로 풀어보자 
        - 최적 부분 문제 -> ai = i를 1로 만드는데 최소 횟수 _ 점화식 : ai = min(ai/5, ai/3, ai/2, ai-1) + 1 (단, 나누어 떨어지는 경우만 연산)
        - 중복 부분 문제 -> a8는 a9구할 때 또 사용됨
[L]
점화식을 로직으로 구현하자
    MAX = 30001
    dp = [0] * MAX
    for i in range(2,MAX):
        if i % 5 == 0:
            dp[i] = dp[i//5] + 1
        elif i % 3 == 0:
            dp[i] = dp[i//3] + 1
        elif i % 2 == 0:
            dp[i] = dp[i//2] + 1
        else:
            dp[i] = dp[i-1] + 1
'''

MAX = 30001


def solve(x):
    dp = [0] * MAX

    for i in range(2, MAX):
        dp[i] = dp[i-1] + 1
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        # dp[i] = min(dp[i], dp[i-1] + 1)

    return dp[x]


X = int(input())

ret = solve(X)

print(ret)
