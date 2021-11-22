'''
> P
길이 N이 주어질 때 게단의 수를 구하라
    - 계단 = 입접한 모든 자리의 차이가 1인 수 
> S
동적 계획법

dp -> 기본 값 = 0 // 크기 = max(101)

ai = 길이가 i인 계단 수 최적의 해
점화식 => ai = (ai-1 * 2) -1, 단, a1 = 9

상향식(bottom-up)
    - param : n(int) _ 길이(입력 값)
    - vari : global dp
    - logic
        1) dp[1] = 9
        2) for i in range(2, MAX) then dp[i] = (dp[i-1] * 2) -1
    

'''


def bottomUp():
    global N

    dp[1] = 9

    for i in range(2, N+1):
        dp[i] = ((dp[i-1] * 2) - 1) % 1000000000

    return dp[N]


N = int(input())
dp = [0] * (N+1)

ret = bottomUp()

print(ret)
